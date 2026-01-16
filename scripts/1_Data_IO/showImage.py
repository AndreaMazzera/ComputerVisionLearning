import cv2 as cv 

# Function to open an image from a given path
def open_image(path: str): 
    
    # Read the image
    img = cv.imread(path)

    if img is None:
        raise FileNotFoundError("Image not found")

    return img

try:
    image = open_image('../assets/images/image.jpg')

    # Display
    cv.imshow("Image", image)

    # Wait for a key press to close the window
    cv.waitKey(0)
    cv.destroyAllWindows()

except FileNotFoundError as e:
    print("Error:", e)