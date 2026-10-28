import cv2
import numpy as np

# Image location
path = r"C:\Users\jaya venkata sai\Downloads\flower.3.webp"

# Read image
img = cv2.imread(path)

if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel operator in X direction
    sobel_x = cv2.Sobel(
        gray, cv2.CV_64F, 1, 0, ksize=3
    )

    # Apply Sobel operator in Y direction
    sobel_y = cv2.Sobel(
        gray, cv2.CV_64F, 0, 1, ksize=3
    )

    # Convert results to 8-bit images
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine horizontal and vertical edges
    result = cv2.addWeighted(
        sobel_x, 0.5, sobel_y, 0.5, 0
    )

    # Display images
    cv2.imshow("Original Flower Image", img)
    cv2.imshow("Sobel X - Vertical Edges", sobel_x)
    cv2.imshow("Sobel Y - Horizontal Edges", sobel_y)
    cv2.imshow("Sobel Edge Detection", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
