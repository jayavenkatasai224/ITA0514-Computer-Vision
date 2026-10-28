import cv2
import numpy as np

# Image location
path = r"C:\Users\jaya venkata sai\Downloads\flower.3.webp"

# Read image
img = cv2.imread(path)

if img is None:
    print("Error: Image not found!")
else:
    rows, cols = img.shape[:2]

    # Four points from the original image
    pts1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Four destination points
    pts2 = np.float32([
        [50, 50],
        [cols - 50, 0],
        [0, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    result = cv2.warpPerspective(img, matrix, (cols, rows))

    # Display images
    cv2.imshow("Original Flower Image", img)
    cv2.imshow("Perspective Transformed Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
