import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Load MoveNet model from TensorFlow Hub
movenet = hub.load("https://tfhub.dev/google/movenet/singlepose/lightning/4")

def run_pose_estimation(frame):
    """Runs pose estimation on a single video frame using MoveNet."""
    # Resize frame to 192x192 for MoveNet
    input_image = tf.image.resize_with_pad(np.expand_dims(frame, axis=0), 192, 192)
    input_image = tf.cast(input_image, dtype=tf.int32)

    # Run pose estimation
    outputs = movenet.signatures['serving_default'](input_image)
    keypoints = outputs['output_0'].numpy()[0, 0, :, :2]  # Extract keypoints

    return keypoints

# Function to visualize keypoints on the frame
def draw_keypoints(frame, keypoints):
    h, w, _ = frame.shape
    for kp in keypoints:
        y, x = int(kp[0] * h), int(kp[1] * w)
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
    return frame
