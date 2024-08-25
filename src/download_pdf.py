import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from logs import logger
import yaml
import logging

logger()
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

# Function to extract and download PDF files
def download_pdfs_from_webpage(url, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Fetch the content of the webpage
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Parse the webpage content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the anchor tags with href attributes ending in .pdf
    pdf_links = soup.find_all('a', href=True)
    pdf_links = [link for link in pdf_links if link['href'].lower().endswith('.pdf')]

    # Download each PDF
    for link in pdf_links:
        # Get the full URL of the PDF
        pdf_url = urljoin(url, link['href'])
        pdf_name = os.path.join(output_dir, os.path.basename(link['href']))

        # Download the PDF
        logging.info(f"Downloading {pdf_url}")
        pdf_response = requests.get(pdf_url)
        pdf_response.raise_for_status()  # Check if the request was successful

        # Save the PDF to the output directory
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)

        logging.info(f"Saved {pdf_name}")

webpage_url = config['WEBPAGE']  
output_directory = config['PDF_PATH']  # Directory where the PDFs will be saved

download_pdfs_from_webpage(webpage_url, output_directory)