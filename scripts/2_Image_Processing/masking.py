import cv2 as cv
import numpy as np

# Read input image from disk
image = cv.imread('assets/images/image.jpg')

# Check if the image was loaded correctly
if image is None:
    raise FileNotFoundError("Image not found")

# --------------------------------------------------
# Create a blank (black) mask
# Same height and width as the image
# Single channel (grayscale)
# --------------------------------------------------
blank = np.zeros(image.shape[:2], dtype=np.uint8)

# --------------------------------------------------
# Draw a white filled circle on the mask
# White (255) represents the region to keep
# Black (0) represents the region to discard
# --------------------------------------------------
mask = cv.circle(
    blank,                                           # Image where the mask is drawn
    (image.shape[1] // 2, image.shape[0] // 2),      # Center of the image (x, y)
    150,                                             # Radius of the circle
    255,                                             # White color → area to keep
    thickness=-1                                     # Filled circle
)

# --------------------------------------------------
# Apply the mask using bitwise AND
# The image is kept only where the mask is white
# --------------------------------------------------
masked_image = cv.bitwise_and(
    image,                   # Source image 1
    image,                   # Source image 2 (same image)
    mask=mask                # Mask controlling which pixels are kept
)

# --------------------------------------------------
# Display results
# --------------------------------------------------
cv.imshow("Original Image", image)
cv.imshow("Masked Image", masked_image)

cv.waitKey(0)
cv.destroyAllWindows()
