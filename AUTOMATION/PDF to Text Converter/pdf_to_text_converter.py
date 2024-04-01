# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:01:17 2024

@author: ncoats
"""

from PyPDF2 import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

def extract_all_PDFs_to_text(filepath):
    for filename in os.listdir(filepath):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(filepath, filename)
            pdf_text = extract_text_from_pdf(pdf_file)
            txt_file = os.path.join(filepath, filename.replace('.pdf', '.txt'))
            save_text_to_file(pdf_text, txt_file)
            print("Text extracted from PDF file and saved to:", txt_file)
            
folder_path = input("Please enter the filepath in which you would like to convert all PDF files to txt files\n")
extract_all_PDFs_to_text(folder_path)

