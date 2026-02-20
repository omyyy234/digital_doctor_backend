"""
Run this to extract everything from your .tflite model file.
It will show you input/output shapes AND try to find class names.

Run with:
    py extract_labels.py
"""
import numpy as np
import json

def extract_model_info(model_path="model.tflite"):
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        from tensorflow.lite.python.interpreter import Interpreter
        interpreter = Interpreter(model_path=model_path)

    interpreter.allocate_tensors()
    input_details  = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print("\n" + "="*55)
    print("  MODEL DETAILS")
    print("="*55)
    print(f"  Input shape : {input_details[0]['shape']}")
    print(f"  Input dtype : {input_details[0]['dtype'].__name__}")
    print(f"  Output shape: {output_details[0]['shape']}")
    print(f"  Num classes : {output_details[0]['shape'][-1]}")

    # Try to read raw flatbuffer bytes to find label strings
    print("\n" + "="*55)
    print("  SEARCHING FOR CLASS NAMES IN MODEL FILE...")
    print("="*55)

    with open(model_path, "rb") as f:
        raw = f.read()

    # Find printable ASCII strings of length 3-40 chars — likely class names
    strings = []
    current = ""
    for byte in raw:
        if 32 <= byte <= 126:
            current += chr(byte)
        else:
            if 3 <= len(current) <= 40:
                strings.append(current)
            current = ""

    # Filter to likely class/label candidates
    skip = {"serving_default", "StatefulPartitionedCall", "dense", "sequential",
            "conv2d", "batch_normalization", "max_pooling", "flatten", "dropout",
            "relu", "softmax", "sigmoid", "input", "output", "float", "uint",
            "TFLITE", "TFL3", "min", "max", "scale", "zero_point"}

    candidates = []
    for s in strings:
        s_clean = s.strip()
        # Skip obvious non-label strings
        if any(kw.lower() in s_clean.lower() for kw in skip):
            continue
        if s_clean.startswith(("_", ".", "/", "\\")):
            continue
        if s_clean.isdigit():
            continue
        # Likely class names: letters, underscores, spaces, hyphens only
        if all(c.isalpha() or c in "_ -()," for c in s_clean):
            candidates.append(s_clean)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    num_classes = output_details[0]['shape'][-1]

    print(f"\n  Found {len(unique)} candidate strings. Showing most likely class names:\n")
    for i, s in enumerate(unique[:60]):
        print(f"  [{i:02d}] {s}")

    print("\n" + "="*55)
    print(f"  Your model has {num_classes} output classes.")
    print(f"  Look at the list above and identify {num_classes} class names.")
    print(f"  Then paste them here and I will create labels.txt for you!")
    print("="*55 + "\n")

if __name__ == "__main__":
    extract_model_info()