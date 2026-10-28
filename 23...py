import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.3.webp")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Top Hat Image", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
