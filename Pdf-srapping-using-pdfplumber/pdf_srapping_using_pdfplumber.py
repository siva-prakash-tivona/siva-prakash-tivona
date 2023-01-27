import pdfplumber
import os
import pandas as pd

file = os.path.join(os.getcwd(), 'Pdf-srapping-using-pdfplumber', 'XBOV11.pdf')
root_folder, file_name = os.path.split(os.path.realpath(__file__))

with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
        table_settings = {
            "vertical_strategy": "text",
            "horizontal_strategy": "text"
        }
        data = page.extract_table(table_settings)

        if pdf.pages.index(page) == 0:
            output_data = data[7::2]
        elif pdf.pages.index(page) == 1:
            extracted_data = data[2::2]
            for d in extracted_data:
                output_data.append(d)
        else:
            extracted_data = data[2:5:2]
            for d in extracted_data:
                list_without_empty_strings= [x for x in d if x]
                if extracted_data.index(d) == 1: # To add two elements together which pdfplumber wrongly read as two data
                    list_without_empty_strings[1] += ''.join(list_without_empty_strings[2])
                    del list_without_empty_strings[2]
                output_data.append(list_without_empty_strings)
                
df = pd.DataFrame(output_data[1::],columns=output_data[0])
os.mkdir(os.path.join(root_folder , file_name[slice(-3)]))
df.to_csv(os.path.join(root_folder , file_name[slice(-3)], 'Pdfplumber-output.csv'), index=False)