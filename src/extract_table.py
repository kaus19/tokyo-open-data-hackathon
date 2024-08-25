import pdfplumber
import re
import yaml
import os
import csv
from logs import logger
import logging

logger()
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

def extract_tables_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Extract text from the first page
            first_page = pdf.pages[0]
            text = first_page.extract_text()

            # Assuming the heading is the first line of text in the PDF
            heading = text.split('\n')[0]
            cleaned_heading = re.sub(r'[\\/*?:"<>|]', "", heading)

            # Define the output CSV file path
            csv_filename = f"{cleaned_heading}.csv"
            tables = []
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    tables.append(table)
            return tables, csv_filename
    except Exception as e:
        logging.error(f"Error occured extracting from pdf {pdf_path}",{e})
    

def save_table_to_csv(tables, csv_filename, output_dir):
    try:
        csv_path = os.path.join(output_dir, csv_filename)
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for table in tables:
                for row in table:
                    writer.writerow(row)
        logging.info(f"Saved CSV: {csv_path}")
    except Exception as e:
        logging.error(f"Error occured saving table to csv {csv_filename}",{e})


def process_pdfs_in_directory(directory_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    i=0
    # List all PDF files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            i = i+1
            pdf_file_path = os.path.join(directory_path, filename)
            logging.info(f"Processing: {pdf_file_path}")
            tables, csv_filename = extract_tables_from_pdf(pdf_file_path)
            if tables:
                save_table_to_csv(tables, f"[{i}]{csv_filename}", output_dir)
            else:
                logging.info(f"No tables found in: {pdf_file_path}")


if __name__ == "__main__":
    pdf_directory_path = config['PDF_PATH']
    output_directory_path = config['CSV_PATH']
    process_pdfs_in_directory(pdf_directory_path, output_directory_path)