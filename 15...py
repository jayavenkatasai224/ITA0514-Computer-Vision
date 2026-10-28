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

    # Convert image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate corner points for better visibility
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Display output
    cv2.imshow("Harris Corner Detection", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
