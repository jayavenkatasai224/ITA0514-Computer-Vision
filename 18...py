import cv2

# Read the image
img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.3.webp")

if img is None:
    print("Image not found")
    exit()

# Select Region of Interest (ROI)
roi = img[50:200, 50:200]

# Copy the ROI
copied_roi = roi.copy()

# Paste the ROI into another region
img[220:370, 220:370] = copied_roi

# Display images
cv2.imshow("Original Image with Pasted ROI", img)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Copied ROI", copied_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
