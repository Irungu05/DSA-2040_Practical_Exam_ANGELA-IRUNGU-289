import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_synthetic_data(num_rows=1000):
    """Generates and saves a synthetic online retail dataset."""

    # Define the data structure based on the exam requirements
    data = {
        'InvoiceNo': ['536365', '536365', '536365'] * (num_rows // 3) + ['536366'] * (num_rows - (num_rows // 3) * 3),
        'StockCode': [f'2{i:04d}' for i in range(num_rows)],
        'Description': [f'Product {i}' for i in range(num_rows)],
        'Quantity': np.random.randint(1, 25, num_rows),
        'InvoiceDate': [datetime.now() - timedelta(days=np.random.randint(0, 365))] * num_rows,
        'UnitPrice': np.random.uniform(1.5, 20.0, num_rows).round(2),
        'CustomerID': np.random.randint(12346, 18287, num_rows),
        'Country': ['United Kingdom', 'France', 'Australia'] * (num_rows // 3) + ['United Kingdom'] * (num_rows - (num_rows // 3) * 3)
    }

    df = pd.DataFrame(data)

    # Add a few rows with missing CustomerID to test the cleaning step
    df.loc[df.sample(frac=0.05).index, 'CustomerID'] = np.nan
    
    df.to_csv('online_retail.csv', index=False)
    print(f"Successfully generated a synthetic 'online_retail.csv' with {num_rows} rows.")

if __name__ == '__main__':
    create_synthetic_data()