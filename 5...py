import cv2
import numpy as np

# Image location
path = r"C:\Users\jaya venkata sai\Downloads\flower.jpg"

# Read image
img = cv2.imread(path)

if img is None:
    print("Error: Image not found!")
else:
    # Create histogram image
    hist_img = np.zeros((400, 512, 3), dtype=np.uint8)

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for i in range(3):
        # Calculate histogram
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])

        # Normalize histogram
        hist = cv2.normalize(
            hist, hist, 0, 350, cv2.NORM_MINMAX
        ).flatten()

        # Draw histogram lines
        for x in range(255):
            y1 = 380 - int(hist[x])
            y2 = 380 - int(hist[x + 1])

            cv2.line(
                hist_img,
                (x * 2, y1),
                ((x + 1) * 2, y2),
                colors[i],
                2
            )

    # Display images
    cv2.imshow("Original Flower Image", img)
    cv2.imshow("Color Histogram", hist_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
