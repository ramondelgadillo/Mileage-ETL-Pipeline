import sqlite3
import pandas as pd

# Function to execute SQL query and return results as DataFrame
def execute_query(query):
    # Connect to SQLite database
    conn = sqlite3.connect('mileage_data.db')

    # Execute query and load results into a DataFrame
    result = pd.read_sql(query, conn)

    # Close the connection
    conn.close()
    return result

if __name__ == "__main__":
    # Example queries

    # Query: Find the percentage of low-mileage cars by brand
    query1 = """
    SELECT brand, 
           SUM(CASE WHEN mileage <= 50000 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS low_mileage_percentage
    FROM cars
    GROUP BY brand;
    """
    data1 = execute_query(query1)
    print("Low mileage percentage by brand:")
    print(data1)

    # Query: Find average price per mileage range
    query2 = """
    SELECT mileage_range, AVG(price) AS avg_price
    FROM cars
    GROUP BY mileage_range;
    """
    data2 = execute_query(query2)
    print("Average price by mileage range:")
    print(data2)

    # Query: Relationship between condition and mileage
    query3 = """
    SELECT condition, AVG(mileage) AS avg_mileage
    FROM cars
    GROUP BY condition;
    """
    data3 = execute_query(query3)
    print("Average mileage by car condition:")
    print(data3)

    # Query: Relationship between condition, price, and mileage
    query4 = """
    SELECT condition, AVG(price) AS avg_price, AVG(mileage) AS avg_mileage
    FROM cars
    GROUP BY condition;
    """
    data4 = execute_query(query4)
    print("Average price and mileage by condition:")
    print(data4)


# Strip whitespace and standardize formatting - This script removes empty space, fixes formatting, and makes the mileage ranges consistent
#df['mileage_range'] = df['mileage_range'].str.strip().str.replace(' ', '').str.upper()