import kagglehub

# Download latest version
path = kagglehub.dataset_download("mubeenshehzadi/customer-churn-dataset")

print("Path to dataset files:", path)