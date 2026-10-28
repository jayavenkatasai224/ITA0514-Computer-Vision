import cv2

# Image location
path = r"C:\Users\jaya venkata sai\Downloads\flower.3.webp"

# Read image
img = cv2.imread(path)

if img is None:
    print("Error: Image not found! Check the file path.")
else:
    # Resize to bigger size
    bigger = cv2.resize(
        img, None,
        fx=2, fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Resize to smaller size
    smaller = cv2.resize(
        img, None,
        fx=0.5, fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
