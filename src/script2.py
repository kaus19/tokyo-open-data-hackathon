import camelot
import pandas as pd

# File path for the uploaded PDF
file_path = 'data/food.pdf'

# Extract tables from the PDF
tables = camelot.read_pdf(file_path, pages='all', flavor='stream')

# Loop through extracted tables
for i, table in enumerate(tables):
    # Export the table to CSV
    df = table.df

    # Handle merging of vertical cells by forward filling the empty cells
    df = df.replace("", pd.NA).ffill(axis=0)

    # Save to CSV
    csv_filename = f"table_{i + 1}.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

    print(f"Table {i + 1} extracted and saved as {csv_filename}")