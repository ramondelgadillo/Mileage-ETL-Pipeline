import pandas as pd

# Load the dataset from the CSV file
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def extract_data():
    # Define the file path for the cleaned data
    cleaned_file = "C:\\Users\\ramon\\Desktop\\Mileage Prediction\\cleaned_cars_data.csv"
    data = load_data(cleaned_file)
    return data

if __name__ == "__main__":
    # If this script is run directly, you can test the extraction
    data = extract_data()
    print(data.head())  # Display the first few rows to ensure the data is loaded correctly

