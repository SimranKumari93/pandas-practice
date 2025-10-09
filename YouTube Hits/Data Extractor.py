import kagglehub

# Download latest version
path = kagglehub.dataset_download("eshummalik/yt-trends")

print("Path to dataset files:", path)