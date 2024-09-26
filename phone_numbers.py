import fitz  # PyMuPDF
import re  # Importar el módulo re

# Open the PDF file
pdf_document = fitz.open("example.pdf")

# Define the regex pattern
pattern = r"\(\d{3}\) \d{3}-\d{4}"

# Iterate through each page
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text = page.get_text()
    matches = re.findall(pattern, text)
    if matches:
        # Print page:phone number in a format like (123) 456-7890
        print(f"Page {page_num + 1}: {matches}")