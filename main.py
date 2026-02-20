"""
🌾 Digital Doctor for Farmers — FastAPI Backend
================================================
Endpoints:
  GET  /              → Health check
  GET  /model-info    → Model details (useful for debugging)
  POST /predict       → Main diagnosis endpoint
  GET  /diseases      → List all known diseases
  GET  /diseases/{id} → Get info for a specific disease
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import time
from config import HOST, PORT

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Digital Doctor for Farmers",
    description="AI-powered crop disease diagnosis API",
    version="1.0.0",
)

# Allow requests from the React Native app (any origin during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load model on startup ─────────────────────────────────────
from model import get_model

@app.on_event("startup")
async def startup_event():
    logger.info("🌱 Starting Digital Doctor API...")
    try:
        model = get_model()
        logger.info(f"✅ Model loaded successfully — {len(model.labels)} classes")
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")
        logger.error("Make sure your .tflite file is in the backend folder and MODEL_PATH in config.py is correct")


# ── Endpoints ─────────────────────────────────────────────────

@app.get("/")
async def health_check():
    """Health check — use this to confirm server is running"""
    return {
        "status": "running",
        "service": "Digital Doctor for Farmers",
        "version": "1.0.0",
        "message": "Server is healthy ✅",
    }


@app.get("/model-info")
async def model_info():
    """Returns model details — run this after starting to verify everything loaded"""
    try:
        model = get_model()
        return {
            "image_size": f"{model.img_height}x{model.img_width}",
            "num_classes": len(model.labels),
            "labels": model.labels,
            "input_dtype": str(model.input_dtype),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    """
    Main diagnosis endpoint.

    Accepts: multipart/form-data with field 'image' (jpg/png)
    Returns: JSON with disease name, confidence, treatment, 7-day action plan
    """
    # Validate file type
    if image.content_type not in ["image/jpeg", "image/jpg", "image/png", "image/webp"]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type: {image.content_type}. Please upload a JPG or PNG image."
        )

    # Read image bytes
    image_bytes = await image.read()

    if len(image_bytes) == 0:
        raise HTTPException(status_code=400, detail="Empty image file received.")

    logger.info(f"Received image: {image.filename}, size: {len(image_bytes)/1024:.1f} KB")

    # Run prediction
    start_time = time.time()
    try:
        model = get_model()
        result = model.predict(image_bytes)
        elapsed = round(time.time() - start_time, 3)

        logger.info(f"Prediction: {result['disease']} ({result['confidence']*100:.1f}%) in {elapsed}s")

        result["inference_time_seconds"] = elapsed
        return JSONResponse(content=result)

    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


@app.get("/diseases")
async def list_diseases():
    """List all diseases the model can detect"""
    from disease_info import PLANTVILLAGE_LABELS, format_label, HEALTHY_LABELS
    diseases = [
        {
            "id": i,
            "raw_label": label,
            "display_name": format_label(label),
            "is_healthy": label in HEALTHY_LABELS,
        }
        for i, label in enumerate(PLANTVILLAGE_LABELS)
    ]
    return {"total": len(diseases), "diseases": diseases}


@app.get("/diseases/{raw_label:path}")
async def get_disease(raw_label: str):
    """Get detailed info for a specific disease by raw label"""
    from disease_info import get_disease_info, get_action_plan, format_label
    info = get_disease_info(raw_label)
    return {
        "raw_label": raw_label,
        "display_name": format_label(raw_label),
        "info": info,
        "action_plan": get_action_plan(raw_label),
    }


# ── Run server ────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*55)
    print("  🌾 Digital Doctor for Farmers — Backend")
    print("="*55)
    print(f"  Server: http://{HOST}:{PORT}")
    print(f"  Docs:   http://localhost:{PORT}/docs")
    print(f"  Test:   http://localhost:{PORT}/model-info")
    print("="*55)
    print("  👉 Find your IP: run 'ipconfig' in CMD")
    print("     Use that IP in your React Native app")
    print("="*55 + "\n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)