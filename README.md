# tokyo open data hackathon 2024

## Overview

Script used for uniforming datasets in [Open Data Hackathon](https://odhackathon.metro.tokyo.lg.jp/en/).  

Make sure you have python and pip installed on your system.

1. Instal the libraries:
```
pip install -r requirements.txt
```

2. Configure `config.yaml` file
    1. PDF_PATH: "data/raw/"
    2. CSV_PATH: "data/result/"
    3. WEBPAGE: "https://www.city.ome.tokyo.jp/site/ome-tky/2389.html"

3. Running script download pdfs from url:
```
python src/download_pdf.py
```

4. Running script to extract csv from pdf:
```
python src/extract_table.py
```

## Folder Structure

Below is a description of the main folders and files in the repository.

```
.
├── data
│   ├── raw
|   |   |──file1.pdf
│   ├── result
|   |   |──file1_result.csv
├── src
│   ├── extract_table.py
│   ├── download_pdf.py
│   ├── logs.py
```


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)