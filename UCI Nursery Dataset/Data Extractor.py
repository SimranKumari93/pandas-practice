import kagglehub

# Download latest version
path = kagglehub.dataset_download("heitornunes/nursery")

print("Path to dataset files:", path)