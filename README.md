# NSDA-Cleaning Project

## Overview

This project analyzes cattle and chicken production data using USDA files. Due to the large size of the dataset, it is processed and filtered using Python scripts and MySQL. The workflow involves chunking the dataset, loading it into MySQL, and running SQL queries to analyze the data.

## Steps

### 1. Data Processing
- **`process_large_dataset.py`**: Filters and reduces the dataset size from 3.5GB to 2.5GB.
- **`chunks.py`**: Splits the reduced dataset into CSV files of 500,000 rows.

### 2. MySQL Setup
- Load each chunk into MySQL using the SQL scripts in the `sql` folder:
  - **`animal_product_csv_load.sql`**: Loads chunks into separate MySQL tables.
  - **`animal_product_queries.sql`**: Contains queries for filtering and analysis.

### 3. Data Cleaning and Aggregation
- **`chicken_summarize.py`**: Replaces empty cells with "UNKNOWN" and aggregates chicken data.
- **`cattle_summarize.py`**: Replaces empty cells with "UNKNOWN" and aggregates cattle data.

## Usage

1. Run `process_large_dataset.py` to filter the raw dataset.
2. Use `chunks.py` to split the data.
3. Load each chunk into MySQL using the SQL queries.
4. Clean and aggregate the data using `chicken_summarize.py` and `cattle_summarize.py`.


You can access a similar USDA dataset for cattle and chicken production by clicking the link below:

[USDA NASS Quick Stats Database](https://quickstats.nass.usda.gov/)
