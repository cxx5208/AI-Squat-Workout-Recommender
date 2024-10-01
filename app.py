from flask import Flask, render_template, request, jsonify
import os
from models.pose_estimation import run_pose_estimation
from models.form_analysis import RepCounter  # Import the RepCounter class
from utils.video_processing import process_video, get_video_fps

app = Flask(__name__)

# Ensure the uploads directory exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files['video']
    video_path = os.path.join("uploads", video.filename)
    video.save(video_path)

    # Process the video frames and get FPS
    frames = process_video(video_path)
    fps = get_video_fps(video_path)

    # Initialize RepCounter
    rep_counter = RepCounter()

    # Analyze each frame and get feedback
    feedbacks = []
    for i, frame in enumerate(frames):
        keypoints = run_pose_estimation(frame)
        form_feedback = rep_counter.analyze_squat_form(keypoints)
        timestamp = round(i / fps, 2)  # Calculate timestamp in seconds

        feedbacks.append({
            "timestamp": timestamp,
            "feedback": form_feedback,
            "reps": rep_counter.get_rep_count()
        })

    return jsonify({"feedback": feedbacks})

if __name__ == '__main__':
    app.run(debug=True)
