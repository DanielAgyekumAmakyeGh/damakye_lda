from damakye_lda import load_dataset, perform_lda

# Use the full path to your dataset
dataset_path = r'C:\Users\Daniel Amakye\Desktop\WineQT.csv'  # Path to your dataset

# Load the dataset
dataset = load_dataset(dataset_path)

# Perform LDA (replace 'target_column_name' with the actual target column name)
result = perform_lda(dataset, 'quality')  # Replace with actual column name

# Print the result of LDA
print(result)
