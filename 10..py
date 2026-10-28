import cv2
import glob
import os

# Downloads folder location
folder = r"C:\Users\jaya venkata sai\Downloads"

# Find Gemini-generated PNG image
files = glob.glob(
    os.path.join(folder, "Gemini_Generated_Image*.png")
)

if not files:
    files = glob.glob(
        os.path.join(folder, "Gemini_Generated_Image*.PNG")
    )

if not files:
    print("Error: Gemini PNG image not found!")
else:
    # Use the matching image
    path = files[0]
    print("Image location:", path)

    img = cv2.imread(path)

    if img is None:
        print("Error: Unable to read image!")
    else:
        # Rotate 90 degrees clockwise
        rotated = cv2.rotate(
            img, cv2.ROTATE_90_CLOCKWISE
        )

        cv2.imshow("Original Image", img)
        cv2.imshow("Rotated Image 90 Degree Clockwise", rotated)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
