import cv2

# Read the image
img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.3.webp")

if img is None:
    print("Image not found")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Display images
cv2.imshow("Original Image", gray)
cv2.imshow("Histogram Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
