import pandas as pd
from sqlalchemy import create_engine
from transform import transform_data

# PostgreSQL credentials
USER = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
HOST = "localhost"
PORT = "5432"
DATABASE = "car_mileage"

def load_data_to_postgres():
    # Get the transformed data
    df = transform_data()

    # Connect to PostgreSQL using SQLAlchemy
    engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

    # Load data into PostgreSQL
    df.to_sql('cars', engine, if_exists='replace', index=False)

    print("Data has been loaded into PostgreSQL database.")

if __name__ == "__main__":
    load_data_to_postgres()
