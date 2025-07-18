import sqlite3
import pandas as pd
from transform import transform_data

# Function to load the data into SQLite database
def load_data_to_sqlite():
    # Get the transformed data
    df = transform_data()

    # Connect to SQLite database (will create it if it doesn't exist)
    conn = sqlite3.connect('mileage_data.db')

    # Create a table and insert data into SQLite
    df.to_sql('cars', conn, if_exists='replace', index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Data has been loaded into SQLite database.")

if __name__ == "__main__":
    load_data_to_sqlite()


