
import cv2

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print("Error: Video not found")
        return

    frames = []

    # Read all video frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("No frames found")
        return

    # Get video properties
    height, width = frames[0].shape[:2]
    fps = 20

    # Create reverse video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        output_path, fourcc, fps, (width, height)
    )

    # Write frames in reverse order
    for frame in reversed(frames):
        out.write(frame)

    out.release()
    print("Reverse video created successfully")

input_path = r"C:\Users\jaya venkata sai\Downloads\gemini_generated_video_586fb452.mp4"
output_path = r"C:\Users\jaya venkata sai\Downloads\reverse_video.mp4"

reverse_video(input_path, output_path)

# Play the reverse video
cap = cv2.VideoCapture(output_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
