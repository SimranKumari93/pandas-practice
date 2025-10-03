import kagglehub

# Download latest version
path = kagglehub.dataset_download("kishanvavdara/subreddit-rules-dataset")

print("Path to dataset files:", path)