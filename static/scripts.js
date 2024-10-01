document.getElementById("uploadForm").addEventListener("submit", function (event) {
    event.preventDefault();  // Prevent the form from submitting normally

    const videoFile = document.getElementById("videoFile").files[0];
    const formData = new FormData();
    formData.append("video", videoFile);

    // Show progress bar
    const progressContainer = document.getElementById("progress-container");
    const progressBar = document.getElementById("progress-bar");
    progressContainer.style.display = "block";

    fetch("/upload", {
        method: "POST",
        body: formData,
        onprogress: function(event) {
            if (event.lengthComputable) {
                const percentComplete = (event.loaded / event.total) * 100;
                progressBar.style.width = percentComplete + '%';
            }
        }
    })
    .then(response => response.json())
    .then(data => {
        progressContainer.style.display = "none";  // Hide progress bar

        // Display the video preview
        const videoElement = document.getElementById("workout-video");
        const videoContainer = document.getElementById("video-container");
        const videoURL = URL.createObjectURL(videoFile);
        document.getElementById("videoSource").src = videoURL;
        videoElement.load();  // Reload the video with the new source
        videoContainer.style.display = "block";  // Make the video player visible

        // Display the feedback in the table
        const feedbackContainer = document.getElementById("feedback-container");
        const feedbackBody = document.getElementById("feedback-body");
        feedbackBody.innerHTML = "";  // Clear existing rows

        data.feedback.forEach(feedback => {
            const row = document.createElement("tr");
            const timestampCell = document.createElement("td");
            const feedbackCell = document.createElement("td");

            timestampCell.textContent = feedback.timestamp;
            feedbackCell.textContent = feedback.feedback.join(", ");  // Join feedback array

            row.appendChild(timestampCell);
            row.appendChild(feedbackCell);
            feedbackBody.appendChild(row);
        });

        feedbackContainer.style.display = "block";  // Show the feedback table
    })
    .catch(error => {
        console.error("Error uploading video:", error);
    });
});

// Dark Mode Toggle
const toggleButton = document.getElementById("dark-mode-toggle");

toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
});
