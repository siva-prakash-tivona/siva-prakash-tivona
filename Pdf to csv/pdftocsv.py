import tabula
import os
import pandas as pd

def pdftocsv_using_tabula(pdf):
    tl = tabula.read_pdf(pdf, pages='all',output_format="dataframe", stream=True)
    df =tl[0].head(15)
    df.to_csv(f"{os.getcwd()}/Pdf to csv/Output_using_tabula.csv", index=False)
    df = pd.read_csv(f"{os.getcwd()}/Pdf to csv/Output_using_tabula.csv", skiprows=1)
    df.to_csv(f"{os.getcwd()}/Pdf to csv/Output_using_tabula.csv", index=False)


if __name__ == '__main__':
    pdf = f'{os.getcwd()}/Pdf to csv/XBOV11.pdf'
    pdftocsv_using_tabula(pdf)