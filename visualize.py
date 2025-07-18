import matplotlib.pyplot as plt
from query import execute_query

# Function to visualize average price by mileage range
def visualize_price_by_mileage():
    query = """
    SELECT mileage_range, AVG(price) AS avg_price
    FROM cars
    GROUP BY mileage_range;
    """
    data = execute_query(query)
    data.plot(kind='bar', x='mileage_range', y='avg_price')
    plt.title('Average Price by Mileage Range')
    plt.xlabel('Mileage Range')
    plt.ylabel('Average Price')
    plt.show()

# Function to visualize percentage of low-mileage cars by brand
def visualize_low_mileage_by_brand():
    query = """
    SELECT brand, 
           SUM(CASE WHEN mileage <= 50000 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS low_mileage_percentage
    FROM cars
    GROUP BY brand;
    """
    data = execute_query(query)
    data.plot(kind='pie', y='low_mileage_percentage', labels=data['brand'], autopct='%1.1f%%')
    plt.title('Percentage of Low-Mileage Cars by Brand')
    plt.show()

if __name__ == "__main__":
    # Visualize results
    visualize_price_by_mileage()
    visualize_low_mileage_by_brand()


