import os
import glob
import pandas as pd

filepaths = glob.glob('invoices/*.xlsx')
print(filepaths)

for i in filepaths:
    df=pd.read_excel(i, sheet_name= "Sheet 1")
    print(df)