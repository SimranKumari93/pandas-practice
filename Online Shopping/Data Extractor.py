import kagglehub

# Download latest version
path = kagglehub.dataset_download("billcampos/online-shoppers")

print("Path to dataset files:", path)  