"""
=============================================================
🔍 STEP 1 — RUN THIS FIRST BEFORE STARTING THE SERVER
=============================================================
This script inspects your .tflite model and tells you:
  - What image size it expects (e.g. 224x224)
  - How many disease classes it can detect
  - Whether you need a labels file

Run with:
    python inspect_model.py --model your_model.tflite

If you also have a labels file:
    python inspect_model.py --model your_model.tflite --labels labels.txt
=============================================================
"""

import argparse
import numpy as np

def inspect_model(model_path: str, labels_path: str = None):
    try:
        import tflite_runtime.interpreter as tflite
        Interpreter = tflite.Interpreter
    except ImportError:
        from tensorflow.lite.python.interpreter import Interpreter

    print("\n" + "="*55)
    print("  🌾 Digital Doctor — Model Inspector")
    print("="*55)

    # Load model
    print(f"\n📂 Loading model: {model_path}")
    interpreter = Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Input details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print("\n📥 INPUT DETAILS:")
    for inp in input_details:
        shape = inp['shape']
        dtype = inp['dtype']
        print(f"   Shape : {shape}")
        if len(shape) == 4:
            _, h, w, c = shape
            print(f"   → Image size expected : {h} x {w} pixels")
            print(f"   → Channels            : {c} ({'RGB' if c == 3 else 'Grayscale' if c == 1 else 'RGBA'})")
        print(f"   → Data type           : {dtype.__name__}")

    print("\n📤 OUTPUT DETAILS:")
    for out in output_details:
        shape = out['shape']
        print(f"   Shape : {shape}")
        if len(shape) == 2:
            num_classes = shape[1]
            print(f"   → Number of disease classes : {num_classes}")

    # Try to load labels
    num_classes = output_details[0]['shape'][1] if len(output_details[0]['shape']) == 2 else None

    if labels_path:
        print(f"\n🏷️  LABELS FILE: {labels_path}")
        with open(labels_path, 'r') as f:
            labels = [line.strip() for line in f.readlines() if line.strip()]
        print(f"   Found {len(labels)} labels:")
        for i, label in enumerate(labels):
            print(f"   [{i:02d}] {label}")
    else:
        print("\n⚠️  NO LABELS FILE PROVIDED")
        if num_classes:
            print(f"   Your model has {num_classes} output classes.")
            print("   Options:")
            print("   1. If it's 38 classes → it's likely the PlantVillage dataset")
            print("      We have built-in labels for this! (see disease_info.py)")
            print("   2. If different → you need to find or create a labels.txt")
            print("      Format: one class name per line, in order")

    # Quick test with dummy input
    print("\n🧪 QUICK TEST (dummy image)...")
    try:
        input_shape = input_details[0]['shape']
        input_dtype = input_details[0]['dtype']
        dummy = np.zeros(input_shape, dtype=input_dtype)
        interpreter.set_tensor(input_details[0]['index'], dummy)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]['index'])
        print(f"   ✅ Model runs successfully!")
        print(f"   Output shape: {output.shape}")
        print(f"   Top predicted class index (dummy): {np.argmax(output)}")
    except Exception as e:
        print(f"   ❌ Error during test: {e}")

    print("\n" + "="*55)
    print("  ✅ Copy these values into config.py:")
    if len(input_details[0]['shape']) == 4:
        _, h, w, _ = input_details[0]['shape']
        print(f"     IMAGE_SIZE = ({h}, {w})")
    if num_classes:
        print(f"     NUM_CLASSES = {num_classes}")
    print("="*55 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, help='Path to your .tflite model file')
    parser.add_argument('--labels', required=False, help='Path to labels.txt (optional)')
    args = parser.parse_args()
    inspect_model(args.model, args.labels)