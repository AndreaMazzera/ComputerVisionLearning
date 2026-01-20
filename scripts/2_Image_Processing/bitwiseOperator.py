import cv2 as cv
import numpy as np

# NOTE: Bitwise operators treat images as binary masks and combine them pixel by pixel.

# Create a black image
blank = np.zeros((400,400), dtype=np.uint8)

# Draw a rectangle
rectangle = cv.rectangle(
    blank.copy(),              # Where the shape will draw
    (30,30),                   # Top-left corner
    (370,370),                 # Down-right corner
    255,                       # Color
    thickness=-1               # Thickness
)

# Draw a circle
circle = cv.circle(
    blank.copy(),              # Where the shape will draw
    (200,200),                 # Center
    200,                       # Radius
    255,                       # Color
    thickness=-1               # Thickness
)

# AND
rect_and_circ = cv.bitwise_and(rectangle, circle)

# OR
rect_or_circ = cv.bitwise_or(rectangle, circle)

# NOT
rect_not = cv.bitwise_not(rectangle)

# XOR
rect_xor_circ = cv.bitwise_xor(rectangle, circle)

# Show Results
cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)
cv.imshow("AND", rect_and_circ)
cv.imshow("OR", rect_or_circ)
cv.imshow("NOT", rect_not)
cv.imshow("XOR", rect_xor_circ)

cv.waitKey(0)
cv.destroyAllWindows()