import os
import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('invoices/*.xlsx')
print(filepaths)

for i in filepaths:
    df = pd.read_excel(i, sheet_name= "Sheet 1")
    print(df)
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.add_page()
    filename= Path(i).stem
    invoice_nr=filename.split("-")[0]
    date=filename.split("-")[1]
    print(filename.split("-"))

    #printing invoice numbers
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=50, h=12, txt=f'INVOICE nr. {invoice_nr}', align="M", ln=1)

    #printing out dates in invoices
    pdf.set_font(family='Times', style='B', size=18)
    pdf.cell(w=50, h=12, txt=f'DATE : {date}', align="M", ln=1)

    #adding table in pdf



    #printing out the pdf
    pdf.output(f'PDFs/{filename}.pdf')

