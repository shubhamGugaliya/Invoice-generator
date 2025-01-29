import os
import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('invoices/*.xlsx')
print(filepaths)

for i in filepaths:
    df = pd.read_excel(i, sheet_name= "Sheet 1")
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()
    filename= Path(i).stem
    invoice_nr=filename.split("-")[0]

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=12, txt=f'INVOICE nr. {invoice_nr}', align="M", ln=1)
    pdf.output(f'PDFs/{filename}.pdf')

