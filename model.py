"""
🧠 ML Model — TFLite Loader & Predictor
"""
import numpy as np
from PIL import Image
import io
import logging
from config import MODEL_PATH, IMAGE_SIZE, CONFIDENCE_THRESHOLD, CUSTOM_LABELS_PATH
from disease_info import PLANTVILLAGE_LABELS, get_disease_info, get_action_plan, format_label

logger = logging.getLogger(__name__)

# ── TFLite Import (Windows compatible) ───────────────────────
try:
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        from tensorflow.lite.python.interpreter import Interpreter
    logger.info("Using tensorflow.lite")
except ImportError:
    raise ImportError("TensorFlow not found. Run: pip install tensorflow")


class CropDiseaseModel:
    def __init__(self):
        logger.info(f"Loading model from: {MODEL_PATH}")
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.interpreter = Interpreter(model_path=MODEL_PATH)
        self.interpreter.allocate_tensors()

        self.input_details  = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        input_shape = self.input_details[0]['shape']
        if len(input_shape) == 4:
            self.img_height = int(input_shape[1])
            self.img_width  = int(input_shape[2])
        else:
            self.img_height, self.img_width = IMAGE_SIZE

        self.input_dtype = self.input_details[0]['dtype']
        logger.info(f"Model expects: {self.img_height}x{self.img_width}, dtype={self.input_dtype.__name__}")

        self.labels = self._load_labels()
        logger.info(f"Loaded {len(self.labels)} class labels")

    def _load_labels(self) -> list:
        if CUSTOM_LABELS_PATH:
            try:
                with open(CUSTOM_LABELS_PATH, 'r') as f:
                    labels = [line.strip() for line in f if line.strip()]
                logger.info(f"Loaded {len(labels)} custom labels from {CUSTOM_LABELS_PATH}")
                return labels
            except FileNotFoundError:
                logger.warning(f"Custom labels file not found: {CUSTOM_LABELS_PATH}")

        num_outputs = self.output_details[0]['shape'][1] if len(self.output_details[0]['shape']) == 2 else 0

        if num_outputs == 38:
            logger.info("Using built-in PlantVillage 38-class labels")
            return PLANTVILLAGE_LABELS

        logger.warning(
            f"Model has {num_outputs} classes but no labels file found.\n"
            f"  Create a labels.txt with {num_outputs} lines and set CUSTOM_LABELS_PATH in config.py"
        )
        return [f"Class_{i}" for i in range(num_outputs)]

    def preprocess(self, image_bytes: bytes) -> np.ndarray:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((self.img_width, self.img_height), Image.LANCZOS)
        arr = np.array(img)

        # YOUR model is uint8 — keep raw pixel values, do NOT divide by 255
        if self.input_dtype == np.float32:
            arr = arr.astype(np.float32) / 255.0
        elif self.input_dtype == np.uint8:
            arr = arr.astype(np.uint8)
        else:
            arr = arr.astype(self.input_dtype)

        return np.expand_dims(arr, axis=0)

    def predict(self, image_bytes: bytes) -> dict:
        input_tensor = self.preprocess(image_bytes)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_tensor)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self.output_details[0]['index'])

        scores = output[0].astype(np.float32)

        # Dequantize uint8 output if needed
        out_detail = self.output_details[0]
        if out_detail['dtype'] == np.uint8:
            scale, zero_point = out_detail['quantization']
            if scale != 0:
                scores = (scores - zero_point) * scale
            # Softmax
            scores = np.exp(scores - np.max(scores))
            scores = scores / scores.sum()

        top_index  = int(np.argmax(scores))
        confidence = float(scores[top_index])

        top3_indices = np.argsort(scores)[-3:][::-1]
        top3 = [
            {
                "label": format_label(self.labels[i]) if i < len(self.labels) else f"Class {i}",
                "raw_label": self.labels[i] if i < len(self.labels) else f"Class_{i}",
                "confidence": round(float(scores[i]), 4),
            }
            for i in top3_indices
        ]

        if confidence < CONFIDENCE_THRESHOLD:
            return {
                "disease": "Unrecognized",
                "raw_label": "unknown",
                "confidence": round(confidence, 4),
                "description": "Could not confidently identify the disease. Please retake in bright natural light with the diseased area filling the frame.",
                "treatment": [
                    "Retake photo in bright natural light",
                    "Ensure the diseased area fills the frame",
                    "Consult your local agricultural officer",
                ],
                "pesticide": "N/A",
                "soil_treatment": "N/A",
                "action_plan": [],
                "top3": top3,
                "status": "low_confidence",
            }

        raw_label   = self.labels[top_index] if top_index < len(self.labels) else f"Class_{top_index}"
        info        = get_disease_info(raw_label)
        action_plan = get_action_plan(raw_label)

        return {
            "disease":        format_label(raw_label),
            "raw_label":      raw_label,
            "confidence":     round(confidence, 4),
            "severity":       info.get("severity", "unknown"),
            "description":    info.get("description", ""),
            "treatment":      info.get("treatment", []),
            "pesticide":      info.get("pesticide", ""),
            "soil_treatment": info.get("soil_treatment", ""),
            "action_plan":    action_plan,
            "top3":           top3,
            "status":         "success",
        }


_model_instance = None

def get_model() -> CropDiseaseModel:
    global _model_instance
    if _model_instance is None:
        _model_instance = CropDiseaseModel()
    return _model_instance