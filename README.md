# 🚗 Car Mileage Analysis - ETL Pipeline

## 📋 Project Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline to analyze car mileage data and its relationship with price, brand, and condition. Using Python and PostgreSQL, the pipeline cleans and processes raw data, stores it in a relational database, executes complex queries for insights, and visualizes key findings with Matplotlib. This demonstrates how ETL pipelines enable scalable, maintainable data analysis workflows without relying on machine learning models.

## ⚡ Features
- Extract raw car data from CSV files and load it into pandas DataFrames.
- Clean and transform data by removing irrelevant columns, handling missing values, and categorizing mileage into ranges.
- Load processed data into a PostgreSQL database with structured schemas.
- Perform SQL queries to analyze trends such as average price by mileage range and mileage distribution by brand.
- Visualize analytical results with charts to enhance interpretability.

## 🛠️ Technologies Used
- **Python** — Data processing and scripting.
- **pandas** — Data manipulation and transformation.
- **PostgreSQL** — Relational database storage and querying.
- **SQLAlchemy & psycopg2** — Database connection and interaction.
- **Matplotlib** — Data visualization.

## 🗂️ Project Structure

Mileage Prediction/
│
├── extract.py # Extract data from CSV
├── transform.py # Transform and clean data
├── load.py # Load data into PostgreSQL
├── query.py # SQL queries for data insights
├── visualize.py # Visualization of query results
├── cleaned_cars_data.csv # Original cleaned CSV dataset
├── transformed_cars_data.csv # Transformed dataset after processing
├── mileage_data.db # PostgreSQL database storing processed data
├── README.md # Project documentation (this file)
└── pycache/ # Python cache files (auto-generated)


## 🔄 ETL Pipeline Overview

Cleaned CSV Data
       │
       ▼
   [EXTRACT] --> extract.py
       │
       ▼
   [TRANSFORM] --> transform.py
       │
       ▼
   [LOAD] --> load.py
       │
       ▼
PostgreSQL Database
       │
       ▼
   [QUERY] --> query.py
       │
       ▼
 [VISUALIZE] --> visualize.py
       │
       ▼
 Charts & Insights

## 🚀 Usage

### Setup
1. Install Python (>=3.7) and dependencies:
```bash

    pip install pandas matplotlib sqlalchemy psycopg2-binary


2. Install PostgreSQL (if not installed)

3. Create a PostgreSQL database:

    CREATE DATABASE car_mileage;


Running the Pipeline

Run the scripts sequentially:

python extract.py       # Loads the raw CSV data
python transform.py     # Cleans and categorizes mileage data
python load.py          # Loads transformed data into PostgreSQL
python query.py         # Executes analytical SQL queries
python visualize.py     # Generates charts from query results

📊 Sample Insights

    Cars with mileage between 0–50K have higher average prices, confirming mileage as a key value factor.

    Mileage distribution varies significantly across car brands, reflecting different usage patterns.

    Visualizations provide clear, actionable insights into pricing trends and mileage ranges

