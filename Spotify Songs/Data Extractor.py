import kagglehub

# Download latest version
path = kagglehub.dataset_download("bwandowando/960k-spotify-songs-lyrics-qwen3-0-6b-embeddings")

print("Path to dataset files:", path)