import cv2

# Read the image
img = cv2.imread(r"C:\Users\jaya venkata sai\Downloads\flower.3.webp")

# Check whether image is loaded
if img is None:
    print("Image not found")
    exit()

# Convert image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

# Save grayscale image
cv2.imwrite(r"C:\Users\jaya venkata sai\Downloads\grayscale_flower.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
