import cv2 as cv
import numpy as np

CONTRIB_MODULES = {
    "face": "Face recognition (LBPH, Eigenfaces, Fisherfaces)",
    "xfeatures2d": "SIFT, SURF (non-free)",
    "bgsegm": "Background subtraction avanzata",
    "optflow": "Optical flow avanzato",
    "tracking": "Tracking avanzato",
    "ximgproc": "Image processing avanzato",
    "aruco": "Marker ArUco",
    "structured_light": "Structured light 3D",
    "saliency": "Saliency detection",
    "text": "OCR e text detection"
}

print("=" * 50)
print(" OpenCV Environment Check")
print("=" * 50)

print(f"OpenCV version : {cv.__version__}")
print(f"NumPy version  : {np.__version__}\n")

print("Checking OpenCV contrib modules:\n")

available = []
missing = []

for module, description in CONTRIB_MODULES.items():
    if hasattr(cv, module):
        available.append(module)
        print(f"[ OK ] {module:<15} - {description}")
    else:
        missing.append(module)
        print(f"[FAIL] {module:<15} - {description}")

print("\n" + "-" * 50)

if not available:
    print("\nYou are probably using 'opencv-python'")
    print("Install with: pip install opencv-contrib-python")
else:
    print(f"Available contrib modules ({len(available)}):")
    print("  " + ", ".join(available))
    
if missing:
    print(f"\nMissing contrib modules ({len(missing)}):")
    print("  " + ", ".join(missing))

print("\nEnvironment check completed.")
print("=" * 50)
