import tabula
import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.append(table)
        return tables

def save_tables_as_csv(tables, output_dir):
    for i, table in enumerate(tables):
        df = pd.DataFrame(table[1:], columns=table[0])
        df.to_csv(f"{output_dir}/table_{i}.csv", index=False)


if __name__ == "__main__":
    pdf_path = "data/raw/step7_errorcode_e.pdf"
    tables = extract_tables_from_pdf(pdf_path)
    # print(tables)
    save_tables_as_csv(tables, "data/processed/")