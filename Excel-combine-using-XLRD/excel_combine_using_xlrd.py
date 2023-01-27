import os
import  xlrd
import datetime
import pandas as pd

def read_excel(pdf):
    wb = xlrd.open_workbook(pdf)
    sheet = wb.sheet_by_index(0)
    output = []
    for i in range(sheet.nrows):
        row = []
        for j in range(sheet.ncols): 
            if i !=0 and j == 0:
                cell = sheet.cell_value(i,j)
                year, month, day, hour, minutes, seconds = xlrd.xldate_as_tuple(cell, wb.datemode)
                date_value = f'{day}/{month}/{year}'
                row.append(date_value)
                continue
            row.append(sheet.cell_value(i,j))
        output.append(row)
    return output

def merge_data(files_data):
    df_list = []
    for file_data in files_data:
        df = pd.DataFrame(file_data[1::],columns=file_data[0])
        df_list.append(df)
    
    output_df  = pd.concat(df_list, ignore_index=True, sort=False)
    output_df.to_csv(os.path.join(os.getcwd(), 'Excel-combine-using-XLRD', 'Merged_Output_data.csv'), index=False)

if __name__ == '__main__':
    files_data = []
    files = os.path.join(os.getcwd(), 'Excel-combine-using-XLRD', 'ExcelFiles')
    for file in os.listdir(files):
        data = read_excel(os.path.join(files, file))
        files_data.append(data)

    merge_data(files_data)