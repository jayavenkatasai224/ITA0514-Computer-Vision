import cv2
import numpy as np

# Read the new flower image
path = r"C:\Users\jaya venkata sai\Downloads\flower.3.webp"
img = cv2.imread(path)

if img is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(gray, kernel, iterations=1)

    # Display original and dilated images
    cv2.imshow("Original Flower Image", gray)
    cv2.imshow("Dilated Flower Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
