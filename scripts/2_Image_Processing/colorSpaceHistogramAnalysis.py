import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

def open_image (imagePath: str):
    image = cv.imread("assets/images/image.jpg")
    if image is None:
        raise FileNotFoundError("Image not found")
    return image

# ===============================================
# Define all images in different color spaces
# ===============================================

# Acquire original BGR image 
try:
    image = open_image("assets/images/image.jpg")
except FileNotFoundError as e:
    print("Error:", e)

# Convert image from BGR to RBG for matplot
rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Convert image from BGR to Grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Converte image from BGR to HSV
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# ===============================================
# Compute colors histongrams  
# ===============================================

# Explanation calcHist parameters:
# --------------------------------------------------
# cv.calcHist(images, channels, mask, histSize, ranges, ...)
#
# images      → list of images to process
#                    - Must be [img] even for a single image
#                    - For BGR/HSV images, pass the original OpenCV image
#                    - For grayscale, pass the gray image
#
# channels    → list of channel indices to compute histogram for
#                    - Grayscale: [0]  → only one channel
#                    - BGR: [0] = Blue, [1] = Green, [2] = Red
#                    - HSV: [0] = Hue, [1] = Saturation, [2] = Value
#
# mask        → optional mask to compute histogram on a region
#                    - None → compute histogram on the entire image
#                    - Otherwise, provide a binary mask
#
# histSize    → list with number of bins per channel
#                    - e.g., [256] → 256 bins for intensity values
#                    - For Hue in HSV, usually [180] (range 0–179)
#
# ranges      → list with min and max intensity values
#                    - Grayscale and BGR channels: [0, 256]
#                    - Hue: [0, 180]
#                    - Saturation/Value: [0, 256]
# 
# --------------------------------------------------

# Original Image Histogram 
blue_channel    =  cv.calcHist([image], [0], None, [256], [0, 256])
green_channel   =  cv.calcHist([image], [1], None, [256], [0, 256])
red_channel     =  cv.calcHist([image], [2], None, [256], [0, 256])

bgr_channels = [blue_channel,  green_channel, red_channel]

# Grayscale Image Histogram  
gray_hist = cv.calcHist([gray_image], [0], None, [256], [0, 256])

# HSV Image Histogram  
hue_channel         =  cv.calcHist([hsv_image], [0], None, [180], [0, 180])
saturation_channel  =  cv.calcHist([hsv_image], [1], None, [256], [0, 256])
value_channel       =  cv.calcHist([hsv_image], [2], None, [256], [0, 256])

hsv_channels = [hue_channel,  saturation_channel, value_channel]

# ===============================================
# Show Results
# ===============================================
fig, axes = plt.subplots(3,2, layout="constrained")
axes = axes.flatten()
color_lines = ('b', 'g', 'r')

axes[0].set_title("Original Image")
axes[0].axis('off')
axes[0].imshow(rgb_image)

axes[1].set_title("Color Histogram (BGR)")
axes[1].set_xlabel("Pixel Intensity")
axes[1].set_ylabel("Number of Pixels")
axes[1].set_xlim([0, 256])
axes[1].grid(True)

bgr_channel_names = ('Blue', 'Green', 'Red')
for i, (name, col) in enumerate(zip(bgr_channel_names, color_lines)):
    axes[1].plot(bgr_channels[i], color=col, label=name)
axes[1].legend()

axes[2].set_title("Grayscale Image")
axes[2].axis('off')
axes[2].imshow(gray_image, cmap='gray')      # Force grayscale

axes[3].set_title('Grayscale Histogram')
axes[3].set_xlabel('Bins')
axes[3].set_ylabel('Number of Pixels')
axes[3].set_xlim([0, 256])
axes[3].grid(True)
axes[3].plot(gray_hist)

axes[4].set_title("HSV Image")
axes[4].axis('off')
axes[4].imshow(hsv_image)

axes[5].set_title("HSV Histogram")
axes[5].set_xlabel("Pixel Intensity")
axes[5].set_ylabel("Number of Pixels")
axes[5].set_xlim([0, 256])
axes[5].grid(True)

hsv_channel_names = ("Hue","Saturation","Value")
for i, (name, col) in enumerate(zip(hsv_channel_names, color_lines)):
    axes[5].plot(hsv_channels[i], color=col, label=name)
axes[5].legend()
    
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()