"""
⚙️  CONFIG — Central configuration for Digital Doctor backend
"""
import os

# ── Model ────────────────────────────────────────────────────
MODEL_PATH = os.getenv("MODEL_PATH", "model.tflite")

# Image size your model expects (auto-detected as 224x224)
IMAGE_SIZE = (224, 224)

# Minimum confidence to trust a prediction
# Below this → returns "Unrecognized" instead of a wrong answer
CONFIDENCE_THRESHOLD = 0.30

# ── Labels ───────────────────────────────────────────────────
# Pointing to our labels.txt
CUSTOM_LABELS_PATH = "labels.txt"

# ── Server ───────────────────────────────────────────────────
HOST = "0.0.0.0"
PORT = 8000