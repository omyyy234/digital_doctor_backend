"""
🧪 API Test Script
==================
Run this AFTER starting the server to verify everything works.

Usage:
    python test_api.py                          # Test with a dummy/solid color image
    python test_api.py --image your_crop.jpg    # Test with a real crop photo
"""
import requests
import json
import argparse
import sys
from io import BytesIO
from PIL import Image

BASE_URL = "http://localhost:8000"

def print_separator(title=""):
    print("\n" + "="*55)
    if title:
        print(f"  {title}")
        print("="*55)

def test_health():
    print_separator("TEST 1: Health Check")
    try:
        r = requests.get(f"{BASE_URL}/")
        r.raise_for_status()
        data = r.json()
        print(f"  ✅ Status: {data['status']}")
        print(f"  ✅ Service: {data['service']}")
    except Exception as e:
        print(f"  ❌ FAILED: {e}")
        print("  Make sure server is running: python main.py")
        sys.exit(1)

def test_model_info():
    print_separator("TEST 2: Model Info")
    try:
        r = requests.get(f"{BASE_URL}/model-info")
        r.raise_for_status()
        data = r.json()
        print(f"  ✅ Image size: {data['image_size']}")
        print(f"  ✅ Number of classes: {data['num_classes']}")
        print(f"  ✅ First 3 labels: {data['labels'][:3]}")
    except Exception as e:
        print(f"  ❌ FAILED: {e}")

def test_predict(image_path=None):
    print_separator("TEST 3: Prediction")
    try:
        if image_path:
            print(f"  Using image: {image_path}")
            with open(image_path, 'rb') as f:
                image_bytes = f.read()
            filename = image_path
            content_type = "image/jpeg"
        else:
            print("  Using dummy green image (no real crop photo provided)")
            # Create a small green test image
            img = Image.new("RGB", (224, 224), color=(34, 139, 34))
            buf = BytesIO()
            img.save(buf, format="JPEG")
            image_bytes = buf.getvalue()
            filename = "test_green.jpg"
            content_type = "image/jpeg"

        files = {"image": (filename, image_bytes, content_type)}
        r = requests.post(f"{BASE_URL}/predict", files=files)
        r.raise_for_status()
        data = r.json()

        print(f"\n  ✅ PREDICTION RESULT:")
        print(f"     Disease     : {data.get('disease', 'N/A')}")
        print(f"     Confidence  : {data.get('confidence', 0)*100:.1f}%")
        print(f"     Severity    : {data.get('severity', 'N/A')}")
        print(f"     Status      : {data.get('status', 'N/A')}")
        print(f"     Infer time  : {data.get('inference_time_seconds', 'N/A')}s")

        if data.get('top3'):
            print(f"\n  Top 3 predictions:")
            for item in data['top3']:
                print(f"     {item['confidence']*100:5.1f}% — {item['label']}")

        if data.get('action_plan'):
            print(f"\n  7-Day Action Plan:")
            for day in data['action_plan']:
                print(f"     Day {day['day']}: {day['task']}")

        print(f"\n  ✅ Full JSON response saved to: test_result.json")
        with open("test_result.json", "w") as f:
            json.dump(data, f, indent=2)

    except Exception as e:
        print(f"  ❌ FAILED: {e}")

def test_diseases_list():
    print_separator("TEST 4: Disease List")
    try:
        r = requests.get(f"{BASE_URL}/diseases")
        r.raise_for_status()
        data = r.json()
        print(f"  ✅ Total diseases in database: {data['total']}")
        print(f"  First 5:")
        for d in data['diseases'][:5]:
            healthy = "🌿 healthy" if d['is_healthy'] else "🔴 disease"
            print(f"     [{d['id']:02d}] {d['display_name']} ({healthy})")
    except Exception as e:
        print(f"  ❌ FAILED: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', required=False, help='Path to a crop image to test with')
    args = parser.parse_args()

    print("\n🌾 Digital Doctor — API Test Suite")
    test_health()
    test_model_info()
    test_predict(args.image)
    test_diseases_list()
    print_separator("ALL TESTS DONE")
    print("  If all ✅ — your backend is ready!")
    print("  Connect your React Native app using your PC's IP address\n")