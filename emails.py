import fitz  # PyMuPDF
import re  # Importar el módulo re

# Open the PDF file
pdf_document = fitz.open("example.pdf")

# Define the regex pattern
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Iterate through each page
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text = page.get_text()
    matches = re.findall(pattern, text)
    if matches:
        # Print page:date
        print(f"Page {page_num + 1}: {matches}")