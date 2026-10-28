import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.jpg")

blur = cv2.GaussianBlur(img, (151, 151), 5)

cv2.imwrite(r"C:\Users\jaya venkata sai\Downloads\blur_flower.jpg", blur)

output = np.hstack((img, blur))

cv2.imshow("Original vs Gaussian Blur", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
