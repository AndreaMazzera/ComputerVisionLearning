import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

# =========================
# Read image
# =========================
image = cv.imread('assets/images/image.jpg')

if image is None:
    raise FileNotFoundError("Image not found")

# =========================
# Convert BGR -> Grayscale
# =========================
# cv.cvtColor converts the image from one color space to another
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# =========================
# Binary Threshold
# =========================
# cv.threshold converts a grayscale image to binary (0 or maxValue)
# Parameters:
# gray          : input grayscale image
# 127           : threshold value (pixels > 127 -> maxValue)
# 255           : maxValue assigned to pixels above the threshold
# cv.THRESH_BINARY : thresholding type (binary: 0 or 255)
_, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# ATTENTION: in case of varying lighting condition, you can also use adaptive thresholding
#_, thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

# =========================
# Find contours
# =========================
# cv.findContours detects contours in a binary image
# Parameters:
# thresh        : input binary image
# cv.RETR_EXTERNAL : retrieval mode
#                   - RETR_EXTERNAL -> only external contours
#                   - RETR_TREE     -> all contours with hierarchy
# cv.CHAIN_APPROX_SIMPLE : contour approximation method
#                   - CHAIN_APPROX_SIMPLE -> stores only necessary points
#                   - CHAIN_APPROX_NONE   -> stores all points
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# =========================
# Draw contours with Threshold
# =========================
# cv.drawContours draws contours on an image
# Parameters:
# output        : image on which to draw
# contours      : list of contours
# -1            : contour index (-1 = draw all)
# (0, 255, 0)   : contour color (green)
# 2             : line thickness
output = image.copy()
cv.drawContours(output, contours, -1, (0, 255, 0), 2)

# =========================
# Draw contours with Canny 
# =========================

canny = cv.Canny(gray, 50, 150)

# =========================
# Show results
# =========================

titles = [
    "Original Image",
    "Threshold",
    "Contours Image with Threshold",
    "Contours Image with Canny"
]

images = [
    image,
    thresh,
    canny,
    output
]

# Visualization
fig, axes = plt.subplots(2, 2, constrained_layout=True)

for ax, img, title in zip(axes.flat, images, titles):
    ax.imshow(img, cmap='gray', vmin=0, vmax=255)
    ax.set_title(title, fontsize=10)
    ax.axis('off')

plt.show()