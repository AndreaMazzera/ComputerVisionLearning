import cv2 as cv
import numpy as np

# Settings
height:int = 600
width:int = 800
channel_numbers: int = 3

# Create a black image
blank = np.zeros((height,width,channel_numbers), dtype=np.uint8)

# Draw manually a white square on the top-left side of black image
blank[1:100,1:100]=255,255,255

# Draw a rectangle
cv.rectangle(
    blank,                      # Where the shape will draw
    (50,100),                   # Top-left corner
    (300,250),                  # Down-right corner
    (255,0,0),                  # Color
    thickness=2                 # Thickness
)

# Draw a line
cv.line(
    blank,                      # Where the shape will draw
    (50,50),                    # Initial Point
    (300,50),                   # Final Point
    (0,255,0),                  # Color
    thickness=2,                # Thickness
)

# Draw a circle
cv.circle(
    blank,                      # Where the shape will draw
    (400,400),                  # Center
    60,                         # Radius
    (0,255,0),                  # Color
    thickness=-1                # Thickness
)

# ATTENTION: thickness=-1 correspont to fill shape case

# Draw text
cv.putText(
    blank,                      # Where the text will draw
    'Test',                     # Text
    (400,400),                  # Position
    cv.FONT_HERSHEY_SIMPLEX,    # Font
    1,                          # Font Scale
    (0,255,255),                # Color
    thickness=2                 # Thickness
) 

cv.imshow("Blank", blank)

cv.waitKey(0)
cv.destroyAllWindows()

