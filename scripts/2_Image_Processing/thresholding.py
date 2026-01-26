import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read input image from disk
image = cv.imread('assets/images/image.jpg')

# Check if the image was loaded correctly
if image is None:
    raise FileNotFoundError("Image not found")

rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Global thresholding
_, thresh1 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
_, thresh2 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
_, thresh3 = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)
_, thresh4 = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
_, thresh5 = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO_INV)

# Otsu
_, otsu = cv.threshold(
    gray, 0, 255,
    cv.THRESH_BINARY + cv.THRESH_OTSU
)

# Adaptive
adaptive = cv.adaptiveThreshold(
    gray, 255,
    cv.ADAPTIVE_THRESH_MEAN_C,
    cv.THRESH_BINARY,
    11, 3
)

titles = [
    'GRAYSCALE',
    'BINARY',
    'BINARY_INV',
    'TRUNC',
    'TOZERO',
    'TOZERO_INV',
    'OTSU',
    'ADAPTIVE'
]

images = [
    gray,
    thresh1,
    thresh2,
    thresh3,
    thresh4,
    thresh5,
    otsu,
    adaptive
]

# Visualization
fig, axes = plt.subplots(2, 4, constrained_layout=True)

for ax, img, title in zip(axes.flat, images, titles):
    ax.imshow(img, cmap='gray', vmin=0, vmax=255)
    ax.set_title(title, fontsize=10)
    ax.axis('off')

plt.show()