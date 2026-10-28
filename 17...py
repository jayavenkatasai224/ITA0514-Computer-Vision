import cv2

# Image location
path = r"C:\Users\jaya venkata sai\Downloads\flower.3.webp"

# Read image
img = cv2.imread(path)

if img is None:
    print("Error: Image not found!")
else:
    # Copy original image
    watermarked = img.copy()

    # Watermark text
    text = "WATERMARK"

    # Get image dimensions
    height, width = img.shape[:2]

    # Set font and position
    font = cv2.FONT_HERSHEY_SIMPLEX
    position = (width - 250, height - 30)

    # Insert watermark
    cv2.putText(
        watermarked,
        text,
        position,
        font,
        1,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
