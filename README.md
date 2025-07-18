# Mileage ETL Pipeline 🚗📊

A lightweight ETL (Extract, Transform, Load) pipeline that processes and analyzes used car data to uncover insights about mileage, pricing, and vehicle condition — all without using machine learning.

## 🧾 Overview

This project builds a full ETL pipeline using Python and SQLite to:

- Clean and structure raw car data
- Analyze trends such as average price by mileage range
- Visualize insights using Matplotlib

It’s designed to show how data analysis and pipelines can provide real value, even without advanced modeling or ML.

## 🛠️ Tools & Technologies

- **Python** – Scripting and orchestration
- **Pandas** – Data cleaning and transformation
- **SQLite** – Lightweight database for storage and querying
- **Matplotlib** – Data visualization

## 📁 Project Structure

mileage-etl-pipeline/
├── extract.py # Load and structure raw CSV data
├── transform.py # Clean and transform data (e.g., create mileage ranges)
├── load.py # Load transformed data into SQLite
├── query.py # Run SQL queries to extract insights
├── visualize.py # Generate visualizations (e.g., avg price by mileage range)
├── cleaned_cars_data.csv # Final cleaned dataset
├── mileage_data.db # SQLite database
└── README.md


## 🚀 How to Run

1. **Install dependencies:**

```bash
pip install pandas matplotlib

    Download or place the dataset:

Place your cleaned dataset (cleaned_cars_data.csv) in the project folder.

    Run the scripts in order:

python extract.py
python transform.py
python load.py
python query.py
python visualize.py

    Explore the results:

    Inspect the database mileage_data.db using any SQLite viewer.

    View generated charts for insights on price and mileage.

📊 Sample Insights

    Cars with lower mileage (0–50K) tend to have significantly higher prices.

    Mileage patterns differ by brand and condition.

    Clean visuals help clarify data trends for quick decision-making.

📌 Key Learnings

    How to build a scalable ETL pipeline using Python and SQLite.

    Importance of clean data and consistent structure in analysis.

    Query optimization and data transformation techniques.
