import cv2
import glob
import os

# Downloads folder location
folder = r"C:\Users\jaya venkata sai\Downloads"

# Find Gemini PNG image
files = glob.glob(
    os.path.join(folder, "Gemini_Generated_Image_2c0w4o2c0w4*.png")
)

if not files:
    files = glob.glob(
        os.path.join(folder, "Gemini_Generated_Image_2c0w4o2c0w4*.PNG")
    )

if not files:
    print("Error: Image not found!")
else:
    path = files[0]
    print("Image location:", path)

    # Read image
    img = cv2.imread(path)

    if img is None:
        print("Error: Unable to read image!")
    else:
        # Rotate 270 degrees clockwise
        rotated = cv2.rotate(
            img, cv2.ROTATE_90_COUNTERCLOCKWISE
        )

        # Display images
        cv2.imshow("Original Image", img)
        cv2.imshow("270 Degree Clockwise Rotation", rotated)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
