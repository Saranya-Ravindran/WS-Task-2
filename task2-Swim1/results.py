import os
import requests
from bs4 import BeautifulSoup
import fitz
url = 'https://www.tnsaa.in/result'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
os.makedirs("pdfs", exist_ok=True)
pdf_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.lower().endswith('.pdf'):
        full_url = requests.compat.urljoin(url, href)
        pdf_links.append(full_url)
print(f"Found {len(pdf_links)} PDF(s).")
for i, pdf_url in enumerate(pdf_links, 1):
    pdf_name = f"pdfs/document_{i}.pdf"
    print(f"Downloading: {pdf_url}")
    pdf_response = requests.get(pdf_url)
    with open(pdf_name, 'wb') as f:
        f.write(pdf_response.content)
for filename in os.listdir("pdfs"):
    if filename.endswith(".pdf"):
        path = os.path.join("pdfs", filename)
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        print(f"\n--- {filename} ---\n{text[:]}")