import cv2
import numpy as np

# Read image from Downloads folder
img = cv2.imread(
    r"C:\Users\jaya venkata sai\Downloads\flower.jpg"
)

if img is None:
    print("Error: Image not found. Check the path.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(gray, kernel, iterations=1)

    # Display original and eroded images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Eroded Image", eroded)

    # Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
