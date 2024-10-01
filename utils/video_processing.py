import cv2

def process_video(video_path):
    """Extract frames from the uploaded video file."""
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames

def get_video_fps(video_path):
    """Get the frames per second (FPS) of the video."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Use OpenCV to retrieve FPS
    cap.release()
    return fps
