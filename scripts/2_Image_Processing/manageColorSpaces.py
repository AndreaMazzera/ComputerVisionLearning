import cv2 as cv 

# Read the image
image = cv.imread('assets/images/image.jpg')

if image is None:
    raise FileNotFoundError("Image not found")

# Space color conversion
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)

# Settings for windows
windows=[
    "BGR (Original)",
    "Grayscale",
    "HSV",
    "LAB"
]

# Show results
for w in windows:
    cv.namedWindow(w, cv.WINDOW_NORMAL)
    cv.resizeWindow(w, 800, 600)
    
cv.imshow("BGR (Original)", image)
cv.imshow("Grayscale", gray)
cv.imshow("HSV", hsv)
cv.imshow("LAB", lab)

# Split BGR channels
b,g,r=cv.split(image)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

merged=cv.merge([b,g,r])
cv.imshow("Recostructed Original Image From Channels BGR",merged)

# Split HSV channels
h,s,v = cv.split(hsv)
cv.imshow("Hue",h)
cv.imshow("Saturation",s)
cv.imshow("Value",v)

# Wait for a key presso to close the windwos
cv.waitKey(0)
cv.destroyAllWindows()
