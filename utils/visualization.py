import matplotlib.pyplot as plt

def plot_progress(progress_data):
    """Visualizes workout progress over time."""
    exercises = list(progress_data.keys())
    values = [progress_data[exercise] for exercise in exercises]

    plt.bar(exercises, values)
    plt.xlabel("Exercises")
    plt.ylabel("Improvement (%)")
    plt.title("Workout Progress")
    plt.show()
