import requests
from bs4 import BeautifulSoup
import streamlit as st
from fpdf import FPDF

# Class to create PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Scraped Data", 0, 1, "C")
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def create_pdf(text, filename):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text.encode('latin-1', 'replace').decode('latin-1'))
    pdf.output(filename, 'F')

# Streamlit app
st.title("Web Scraping and PDF Generation")

url = st.text_input("Enter URL to scrape:")
if url:
    # Scrape the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    
    # Clean the text
    cleaned_text = ' '.join(text.split())
    
    # Display the cleaned text
    st.write(cleaned_text)
    
    # Save to PDF
    create_pdf(cleaned_text, "output.pdf")
    st.success("PDF created successfully!")
