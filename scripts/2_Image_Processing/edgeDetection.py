import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read input image from disk
image = cv.imread('assets/images/image.jpg')

# Check if the image was loaded correctly
if image is None:
    raise FileNotFoundError("Image not found")

# Convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# --------------------------------------------------
# Apply Laplacian edge detection
# Use CV_64F to avoid overflow (negative values)
# --------------------------------------------------
lap = cv.Laplacian(gray, cv.CV_64F)

# Convert to absolute values and then to uint8
lap = np.uint8(np.absolute(lap))

# Canny
canny = cv.Canny(gray, 150, 175)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobels = cv.bitwise_or(sobelx,sobely)

# --------------------------------------------------
# Display results
# --------------------------------------------------

titles = [
    "Grayscale Image",
    "Laplacian",
    "Canny",
    "Sobel X",
    "Sobel Y",
    "Sobel Combined"
]

images = [
    gray,
    lap,
    canny,
    sobelx,
    sobely,
    combined_sobels
]

# Visualization
fig, axes = plt.subplots(2, 3, constrained_layout=True)

for ax, img, title in zip(axes.flat, images, titles):
    ax.imshow(img, cmap='gray', vmin=0, vmax=255)
    ax.set_title(title, fontsize=10)
    ax.axis('off')

plt.show()