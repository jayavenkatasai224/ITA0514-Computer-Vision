import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.3.webp")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Opening Image", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
