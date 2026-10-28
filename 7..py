import cv2

# Video file location
path = r"C:\Users\jaya venkata sai\Downloads\gemini_generated_video_586fb452.mp4"

# Open video
cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Error: Video not found!")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    # Calculate playback delays
    normal_delay = max(1, int(1000 / fps))
    slow_delay = normal_delay * 2
    fast_delay = max(1, normal_delay // 2)

    # Slow motion
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Slow Motion Video", frame)

        if cv2.waitKey(slow_delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Reopen video for fast motion
    cap = cv2.VideoCapture(path)

    # Fast motion
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Fast Motion Video", frame)

        if cv2.waitKey(fast_delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
