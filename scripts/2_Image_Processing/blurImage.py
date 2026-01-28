import cv2 as cv
import matplotlib.pyplot as plt

def open_image(path: str): 
    img = cv.imread(path)
    if img is None:
        raise FileNotFoundError("Image not found")
    return img

try:
    image = open_image('assets/images/image.jpg')

    # Mean Blur (Averaging filter):
    # each pixel is replaced by the average value of its neighbors
    blur_mean_image = cv.blur(image, (7, 7))

    # Gaussian Blur:
    # uses a Gaussian kernel -> central pixels have higher weight
    g_blurred_image = cv.GaussianBlur(image, (7, 7), 0)

    # Median Blur:
    # replaces each pixel with the median of the neighborhood
    # very effective for salt-and-pepper noise
    blur_median_image = cv.medianBlur(image, 7)

    # Bilateral Filter:
    # smooths the image while preserving edges
    # d           -> diameter of the pixel neighborhood
    # sigmaColor  -> filter sigma in the color space
    # sigmaSpace  -> filter sigma in the coordinate space
    blur_bilateral_image = cv.bilateralFilter(
        image,
        d=9,
        sigmaColor=75,
        sigmaSpace=75
    )

    # Box Filter:
    # ddepth  -> depth of the output image (-1 means same as input)
    # ksize   -> size of the kernel (width, height)
    # normalize -> if True, the kernel is normalized (similar to mean blur)
    #              if False, pixel values are not scaled (rarely used)
    blur_box_image = cv.boxFilter(
        image,
        ddepth=-1,
        ksize=(7, 7),
        normalize=True
    )

    # Convert BGR to RGB for matplotlib
    images = [
        cv.cvtColor(image, cv.COLOR_BGR2RGB),
        cv.cvtColor(blur_mean_image, cv.COLOR_BGR2RGB),
        cv.cvtColor(g_blurred_image, cv.COLOR_BGR2RGB),
        cv.cvtColor(blur_median_image, cv.COLOR_BGR2RGB),
        cv.cvtColor(blur_bilateral_image, cv.COLOR_BGR2RGB),
        cv.cvtColor(blur_box_image, cv.COLOR_BGR2RGB)
    ]

    titles = [
        "Original",
        "Mean Blur",
        "Gaussian Blur",
        "Median Blur",
        "Bilateral Filter",
        "Box Filter"
    ]

    # Create 2x3 subplot
    plt.figure(figsize=(12, 8))

    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()

except FileNotFoundError as e:
    print("Error:", e)
