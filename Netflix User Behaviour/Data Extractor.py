import kagglehub

# Download latest version
path = kagglehub.dataset_download("sayeeduddin/netflix-2025user-behavior-dataset-210k-records")

print("Path to dataset files:", path)