import kagglehub

# Download latest version
path = kagglehub.dataset_download("adharshinikumar/screentime-vs-mentalwellness-survey-2025")

print("Path to dataset files:", path)