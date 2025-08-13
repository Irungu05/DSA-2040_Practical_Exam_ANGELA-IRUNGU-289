# etl_retail.py

import pandas as pd
import sqlite3

def extract_and_transform(file_path):
    """
    Extracts data from an Excel file, transforms it, and returns DataFrames
    for dimension and fact tables.
    """
    # 1. Read the data from the Excel file
    # The read_excel function is used to handle .xlsx files
    df = pd.read_excel(file_path, engine='openpyxl')

    # 2. Perform transformations
    # - Handle missing values (e.g., drop rows with missing CustomerID)
    df = df.dropna(subset=['CustomerID'])

    # - Correct data types (e.g., convert InvoiceDate to datetime)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # - Create new columns (e.g., TotalSales)
    df['TotalSales'] = df['Quantity'] * df['UnitPrice']

    # - Filter out irrelevant data (e.g., negative quantities)
    df = df[df['Quantity'] > 0]
    
    # 3. Create DataFrames for your dimension and fact tables
    customer_dim = df[['CustomerID', 'Country']].drop_duplicates()
    product_dim = df[['StockCode', 'Description', 'UnitPrice']].drop_duplicates()
    
    # Create the TimeDim table from the InvoiceDate
    time_dim = pd.DataFrame(df['InvoiceDate'].drop_duplicates().sort_values())
    time_dim.columns = ['FullDate']
    time_dim['Year'] = time_dim['FullDate'].dt.year
    time_dim['Quarter'] = time_dim['FullDate'].dt.quarter
    time_dim['Month'] = time_dim['FullDate'].dt.month
    time_dim['Day'] = time_dim['FullDate'].dt.day
    time_dim['DayOfWeek'] = time_dim['FullDate'].dt.day_name()
    
    # Create the SalesFact table with foreign keys
    sales_fact = df[['InvoiceNo', 'StockCode', 'CustomerID', 'InvoiceDate', 'Quantity', 'TotalSales']]
    
    return customer_dim, product_dim, time_dim, sales_fact

def load_data(customer_df, product_df, time_df, sales_df):
    """
    Creates the database and loads the DataFrames into tables.
    """
    conn = sqlite3.connect('retail_dw.db')
    cursor = conn.cursor()

    with open('create_tables.sql', 'r') as f:
        sql_script = f.read()
    cursor.executescript(sql_script)

    customer_df.to_sql('CustomerDim', conn, if_exists='replace', index=False)
    product_df.to_sql('ProductDim', conn, if_exists='replace', index=False)
    time_df.to_sql('TimeDim', conn, if_exists='replace', index=False)
    sales_df.to_sql('SalesFact', conn, if_exists='replace', index=False)
    
    conn.close()
    print("ETL process complete. Data loaded into retail_dw.db.")

def main():
    # Define the file path as a variable, using forward slashes or a raw string
    file_path = "C:/Users/Kabura/OneDrive/Desktop/endsemproject/online_retail.csv.xlsx"
    
    try:
        # Call the function and pass the file_path variable to it
        customer_df, product_df, time_df, sales_df = extract_and_transform(file_path)
        load_data(customer_df, product_df, time_df, sales_df)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please make sure it is in the correct location.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()