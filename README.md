
# Regex Search Repository

![GitHub Created At](https://img.shields.io/github/created-at/gabimin/regex-pdf-search?style=flat-square&logoSize=auto&labelColor=black&color=teal)

This repository contains scripts to search for specific patterns in text files using regular expressions. The patterns include email addresses, phone numbers, and dates.

## Files

- emails.py

This script searches for email addresses in the format <example@example.com>.

Regex Pattern: r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

- phone_numbers.py

This script searches for phone numbers in the format (123) 456-7890.

Regex Pattern: r"\(\d{3}\) \d{3}-\d{4}"

- dates.py

This script searches for dates in the format YYYY-MM-DD.

Regex Pattern: r"\d{4}-\d{2}-\d{2}"

## Clone

git clone <https://github.com/gabimin/regex-pdf-search.git>

cd regex-pdf-search

## Run the scripts

For searching emails:
python3 emails.py

For searching phone numbers:
python3 phone_numbers.py

For searching dates:
python3 dates.py

## Requirements

- Python 3.x
- re module (standard library for regex)
- fitz (installation command: pip install PyMuPDF)
