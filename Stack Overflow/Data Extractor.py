import kagglehub

# Download latest version
path = kagglehub.dataset_download("berkayalan/stack-overflow-annual-developer-survey-2024")

print("Path to dataset files:", path)  