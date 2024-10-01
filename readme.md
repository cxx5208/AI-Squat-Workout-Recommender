# AI-Squat-Workout-Recommender

## Overview

The **AI-Squat-Workout-Recommender** is an artificial intelligence-based system designed to evaluate squat form and provide workout recommendations. The system uses human pose estimation models to track the user's movements in videos and detects squat form deficiencies by analyzing key joint angles. Based on this analysis, it recommends corrective exercises.


![Chat Groc Demo](https://img.youtube.com/vi/RTCbG9Q8kmI/0.jpg)  
[Watch the Demo](https://www.youtube.com/watch?v=RTCbG9Q8kmI) 

## Tech Stack

The project employs a variety of technologies, libraries, and models to perform pose estimation, video processing, and workout recommendation generation.

### Backend Technologies

- **Python 3.7+**: The core programming language used for all logic and model execution.
- **Flask**: A lightweight web framework used for the web server, enabling file uploads (user videos), and providing user interaction via the browser.
- **OpenCV**: An open-source library for handling video input, converting videos into frames, and preprocessing image data for model input.
- **PyTorch**: Deep learning framework used to load and perform inference with pre-trained models for pose estimation and possibly form classification.
- **Mediapipe (Optional)**: A library for real-time human pose estimation that can be used as an alternative to custom-trained models.
- **NumPy/Pandas**: Libraries used for numerical computation and data processing, including handling model outputs (keypoint data) and performing analysis on them.
- **Matplotlib**: For visualization purposes, particularly when rendering the pose estimation results (keypoints) overlaid on the video frames.

### Frontend Technologies

- **HTML5, CSS, JavaScript**: Standard web technologies for building the web interface, which allows users to upload videos and view feedback.
- **Bootstrap**: Used for responsive UI design in the web app.
- **Jinja2**: Flask's templating engine for rendering dynamic content on the web page.

## Models Used

The AI-Squat-Workout-Recommender heavily relies on machine learning models for **pose estimation** and **form analysis**. Below are the core models integrated into the system.

### 1. **Pose Estimation Model**

This is the heart of the system, responsible for detecting human keypoints (joints such as hips, knees, and ankles) from the uploaded squat videos. The keypoints are used to compute joint angles and evaluate the user's squat form.

- **Pre-trained Model**: The system uses a pre-trained deep learning model for human pose estimation. This could either be:
  - **OpenPose**: A widely-used neural network model for real-time pose detection, trained on datasets like COCO and MPII.
  - **Mediapipe**: A Google solution for real-time human pose tracking, which provides a lightweight alternative to OpenPose.

These models output a set of **keypoints** (x, y coordinates for each joint) for each frame in the video, which are later used to assess form errors.

#### Input:
- RGB frames extracted from the user’s video.

#### Output:
- 2D coordinates of key joints, such as the hip, knee, and ankle.

#### Example:
For a frame, the model might output a set of coordinates like this for each detected joint:
```
[
  {joint: 'hip', x: 0.45, y: 0.75},
  {joint: 'knee', x: 0.47, y: 0.95},
  {joint: 'ankle', x: 0.48, y: 1.0}
]
```

### 2. **Squat Analysis Engine**

This module processes the output from the pose estimation model to evaluate the user's squat form.

#### Key Functions:
- **Angle Calculation**: The system computes the angles between key joints (hip, knee, and ankle) to assess the depth, alignment, and overall form of the squat.
  - Example: Hip-Knee-Ankle angle to determine the depth of a squat.
  
- **Error Detection**: The calculated angles are compared with pre-defined "ideal" squat angles to detect form errors such as:
  - **Knee Valgus**: When the knees cave inward.
  - **Forward Lean**: Excessive forward movement of the torso.
  - **Shallow Squat**: Insufficient depth when performing a squat.

### 3. **Recommendation System**

The recommendation engine is designed to suggest corrective exercises based on the form errors detected by the squat analysis engine. It uses a rule-based approach (or potentially a decision tree model) to map detected errors to specific workouts.

- **Rule-Based Logic**: Based on the detected issues, the system selects corrective exercises stored in the `workouts/` directory. Each form error corresponds to one or more corrective exercises.
  
- **Future Enhancement**: The system can potentially be enhanced by integrating a machine learning-based recommendation system, trained on large datasets of user form data.

#### Example:
If the system detects **knee valgus** (knees caving inward), it may recommend:
- Lateral Band Walks
- Clamshells
- Glute Bridges

## Data Flow and Processing

### 1. Video Upload and Preprocessing
- The user uploads a video through the Flask-based web interface.
- OpenCV extracts frames from the video, which are then resized and normalized for model input.
  
### 2. Pose Estimation
- The pre-trained pose estimation model processes each frame to detect keypoints (e.g., hips, knees, ankles) and outputs the joint coordinates.

### 3. Squat Form Analysis
- The system calculates relevant angles from the detected keypoints.
- It compares these angles against predefined ideal forms to detect errors such as improper squat depth, knee valgus, or excessive forward lean.

### 4. Recommendation Generation
- Based on the detected form errors, the system consults a rule-based engine that outputs corrective exercises.
- The recommendations are displayed to the user on the web interface along with visualizations of the squat keypoints.

## Running the System

### Step-by-Step Guide:

1. **Install Dependencies**:
   Install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download or Load Models**:
   Ensure that the pose estimation model (either OpenPose or Mediapipe) is available in the `models/` directory. Pre-trained models can be downloaded from relevant sources if not included.

3. **Start the Flask Application**:
   To start the server, run:
   ```bash
   python app.py
   ```

4. **Upload a Video**:
   - Go to `http://127.0.0.1:5000` in your web browser.
   - Upload a video for analysis (must contain a person performing squats).
   
5. **Receive Feedback**:
   - The system will process the video and provide visual feedback on the detected keypoints.
   - A detailed analysis of the squat form, including detected errors and corrective workout recommendations, will be displayed.

## Conclusion

The **AI-Squat-Workout-Recommender** is built using cutting-edge technologies in pose estimation and machine learning to provide personalized fitness recommendations. The system can be expanded to include more exercises and form checks, along with enhancements in real-time analysis using webcam inputs.

By leveraging powerful deep learning models for pose detection and a robust recommendation engine, the system offers practical feedback to help users improve their workout technique.
