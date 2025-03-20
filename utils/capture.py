import cv2

def capture_frames(source="save.mp4"):
    cap = cv2.VideoCapture(source)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
