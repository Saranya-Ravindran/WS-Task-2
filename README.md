# WS-Task-2: Regional Sports Data Scraper

This project scrapes event results and performance records from regional sports boards:
- Indian Badminton Association
- Tamil Nadu Swimming Association

The repository includes scripts to extract data, PDFs downloaded from the sites, and compiled Word documents.

## Repository Layout

WS-Task-2/
│
├── swim_pdfs/ # Downloaded individual swimming PDFs
│
├── task2-Bad2.py # Badminton results scraper
├── task2-Swim1.py # Swimming results/records scraper
│
├── scraped_task2-bad_records.docx # Compiled badminton results
├── scraped_task2-swim_records.docx # Compiled swim records
├── scraped_task2-swim_results.docx # Compiled swim competition results
│
└── requirements.txt # Python dependencies

## Library Dependencies

All scripts rely on these Python libraries:

- `requests` for downloading web pages and PDFs  
- `beautifulsoup4` for HTML parsing  
- `PyPDF2` or `pdfplumber` for extracting PDF text  
- `python-docx` for creating and writing `.docx` files  
- `os`, `glob` for handling file operations

Install everything using:

pip install -r requirements.txt

# Scripts and Outputs: 

task2-Bad2.py :
Scrapes badminton match results.
Final document: scraped_task2-bad_records.docx.

task2-Swim1.py
Downloads swimming PDFs to swim_pdfs/.
Parses and extracts results and records.

Outputs two documents:
scraped_task2-swim_results.docx (competition results)
scraped_task2-swim_records.docx (performance records)

How to Run
Clone the repository.
Install dependencies.

Run:
python task2-Bad2.py
python task2-Swim1.py
Check the generated .docx files for structured data output.
