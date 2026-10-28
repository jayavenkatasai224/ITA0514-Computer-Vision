import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.jpg")

blur = cv2.GaussianBlur(img, (1,1), 5)
blur1 = cv2.GaussianBlur(img, (151,151), 15)
blur2= cv2.GaussianBlur(img, (251,251), 25)
blur3 = cv2.GaussianBlur(img, (351,351), 35)
output = np.hstack((img, blur))
output1 = np.hstack((img, blur1))
output2 = np.hstack((img, blur2))
output3 = np.hstack((img, blur3))

cv2.imshow("Original vs Gaussian Blur", output)
cv2.imshow("Original vs Gaussian Blur1", output1)
cv2.imshow("Original vs Gaussian Blur2", output2)
cv2.imshow("Original vs Gaussian Blur3", output3)
cv2.waitKey(0)
cv2.destroyAllWindows()

