import numpy as np

def calculate_angle(p1, p2, p3):
    """Calculates the angle between three points (used to check form)."""
    a = np.linalg.norm(p2 - p1)
    b = np.linalg.norm(p2 - p3)
    c = np.linalg.norm(p3 - p1)
    angle = np.arccos((a**2 + b**2 - c**2) / (2 * a * b))
    return np.degrees(angle)

class RepCounter:
    def __init__(self, exercise_type="squat"):
        self.exercise_type = exercise_type
        self.rep_count = 0
        self.is_squatting = False  # Track the current state (up or down)


    def analyze_squat_form(self, keypoints):
        """Analyzes squat form and counts reps based on knee angles."""
        left_hip, left_knee, left_ankle = keypoints[11], keypoints[13], keypoints[15]
        right_hip, right_knee, right_ankle = keypoints[12], keypoints[14], keypoints[16]  # Corrected the index for right_ankle

        # Calculate knee angles
        left_knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
        right_knee_angle = calculate_angle(right_hip, right_knee, right_ankle)

        feedback = []
        avg_knee_angle = (left_knee_angle + right_knee_angle) / 2

        # Check squat depth
        if avg_knee_angle >= 90:
            feedback.append("Squat deeper to improve form.")
        else:
            feedback.append("Good squat depth!")

        # Count reps
        self.count_reps(avg_knee_angle)

        # Additional feedback
        if abs(left_knee[0] - left_ankle[0]) > 30 or abs(right_knee[0] - right_ankle[0]) > 30:
            feedback.append("Keep your knees aligned with your toes.")

        return feedback


    def count_reps(self, knee_angle):
        """Count reps based on knee angle."""
        # Thresholds for squatting down and standing up
        squat_threshold = 80
        stand_threshold = 160

        if self.is_squatting and knee_angle > stand_threshold:
            # Transition from squatting to standing
            self.is_squatting = False
            self.rep_count += 1  # Increment the rep count
        elif not self.is_squatting and knee_angle < squat_threshold:
            # Transition from standing to squatting
            self.is_squatting = True

    def get_rep_count(self):
        """Returns the current rep count."""
        return self.rep_count
