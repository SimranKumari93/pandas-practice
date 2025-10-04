import kagglehub

# Download latest version
path = kagglehub.dataset_download("codebynadiia/gdp-by-country-20052025-20-years-of-global-data")

print("Path to dataset files:", path)