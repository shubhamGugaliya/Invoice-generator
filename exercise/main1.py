from fpdf import FPDF
import os
import glob

filepath = glob.glob('*.txt')



for i in filepath:
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_display_mode('fullwidth')
    pdf.add_page()
    pdf.cell(w=50, h=12, txt=i.split('.txt')[0].capitalize(), align="M", ln=1)
    print(i)

    with open(i, 'r',errors="ignore") as textfile:
        content=textfile.read()
    pdf.set_font(family='Times', size=10)
    pdf.multi_cell(w=200, h=5, txt=content, align="M")
    pdf.output(f'output_pdf/{i.split('.txt')[0]}.pdf')






