import pandas as pd
from extract import extract_data

# Function to transform the data (e.g., cleaning, adding new columns)
def transform_data():
    # Extract data
    df = extract_data()

    # Clean the data (drop unnecessary columns, fill missing values, etc.)
    df = df.drop(columns=['unnamed:_0'])  # Remove unnamed column
    df['mileage_range'] = pd.cut(df['mileage'], bins=[0, 50000, 100000, 150000, 200000, float('inf')],
                                 labels=['0-50K', '50K-100K', '100K-150K', '150K-200K', '200K+'])
    df = df.dropna()  # Drop rows with missing values (if any)

    # Return the transformed data
    return df

# Transform the data and save it to a new CSV file
transformed_data = transform_data()
transformed_data.to_csv('transformed_cars_data.csv', index=False)
print("Data has been transformed and saved.")



