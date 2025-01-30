import os
import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('invoices/*.xlsx')
print(filepaths)

for i in filepaths:
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
    df = pd.read_excel(i, sheet_name= "Sheet 1")
    columns=df.columns
    columns=[item.replace("_"," ").title() for item in columns]
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=30, h=8, txt=f'{columns[0]}', align="M", border=1)
    pdf.cell(w=50, h=8, txt=f'{columns[1]}', align="M", border=1)
    pdf.cell(w=40, h=8, txt=f'{columns[2]}', align="M", border=1)
    pdf.cell(w=30, h=8, txt=f'{columns[3]}', align="M", border=1)
    pdf.cell(w=30, h=8, txt=f'{columns[4]}', align="M", border=1, ln=1)

    for index,row in df.iterrows():
        pdf.set_font(family='Times', style='B', size=8)
        pdf.cell(w=30, h=8, txt=f'{row['product_id']}', align="M",border=1)
        pdf.cell(w=50, h=8, txt=f'{row['product_name']}', align="M",border=1)
        pdf.cell(w=40, h=8, txt=f'{row['amount_purchased']}', align="M",border=1)
        pdf.cell(w=30, h=8, txt=f'{row['price_per_unit']}', align="M",border=1)
        pdf.cell(w=30, h=8, txt=f'{row['total_price']}', align="M",border=1,ln=1)
        print(index)
        print(row)

    pdf.set_font(family='Times', style='B', size=8)
    pdf.cell(w=30, h=8, txt='', align="M", border=1)
    pdf.cell(w=50, h=8, txt='', align="M", border=1)
    pdf.cell(w=40, h=8, txt='', align="M", border=1)
    pdf.cell(w=30, h=8, txt='', align="M", border=1)
    pdf.cell(w=30, h=8, txt=f'{df["total_price"].sum()}', align="M", border=1, ln=1)

#writing the summary in pdf
    pdf.set_font(family='Times', style='B', size=10)
    pdf.cell(w=80, h=8, txt=f'The total price is {df["total_price"].sum()} ', align="M", ln=1)

    #add company name and logo
    pdf.cell(w=30, h=8, txt=f'Shubham Gugaliya', align="M")
    pdf.image("images/pythonhow.png",w=10)

    #printing out the pdf
    pdf.output(f'PDFs/{filename}.pdf')

