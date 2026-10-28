import cv2
import glob
import os
import numpy as np

# Image location
folder = r"C:\Users\jaya venkata sai\Downloads"

files = glob.glob(
    os.path.join(folder, "Gemini_Generated_Image_2c0w4o2c0w4*.png")
)

if not files:
    files = glob.glob(
        os.path.join(folder, "Gemini_Generated_Image_2c0w4o2c0w4*.PNG")
    )

if not files:
    print("Error: Image not found!")
else:
    img = cv2.imread(files[0])

    if img is None:
        print("Error: Unable to read image!")
    else:
        rows, cols = img.shape[:2]

        # Three original points
        pts1 = np.float32([
            [50, 50],
            [200, 50],
            [50, 200]
        ])

        # Three destination points
        pts2 = np.float32([
            [10, 100],
            [200, 50],
            [100, 250]
        ])

        # Calculate affine transformation matrix
        matrix = cv2.getAffineTransform(pts1, pts2)

        # Apply affine transformation
        result = cv2.warpAffine(img, matrix, (cols, rows))

        # Display images
        cv2.imshow("Original Image", img)
        cv2.imshow("Affine Transformed Image", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
