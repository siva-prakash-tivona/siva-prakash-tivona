import pandas as pd
import os
import csv

def compute_location(row):
    if '-' in row['constituent_ticker']:
        ticker = row['constituent_ticker'].split('-')
        return ticker[1]
    else:
        return ''

def compute_date(row):
    splited_date = row['as_of_date'].split('-')
    if splited_date[1] == 'Nov':
        return f'{splited_date[2]}-11-{splited_date[0]}'

def build_dataframe(excel_path):
    excel_list = os.listdir(excel_path)
    df_list = []
    for excel in excel_list:
        excel_file_path = f'{os.getcwd()}/combine-csv-data/Excelsheets/{excel}'
        df = pd.read_excel(excel_file_path)
        df_list.append(df)
    output_dataframe = pd.concat(df_list, ignore_index=True)
    output_dataframe.rename(columns = {'Name':'constituent_name',
                                    'Weight (%)' : 'weighting_sponsor',
                                    'Identifier' : 'constituent_ticker',
                                    'ISIN' : 'isin',
                                    'SEDOL' : 'sedol',
                                    'Shares Held' : 'quantity_held',
                                    'Base Market Value' : 'market_value_held',
                                    'Local Currency' : 'local_currency',
                                    'Local Price' : 'local_price',
                                    'Holdings As of' : 'as_of_date'}, inplace = True)
    output_dataframe['weighting_sponsor'] = output_dataframe['weighting_sponsor'].div(100)
    output_dataframe.replace('Unassigned', 'None', inplace=True)
    output_dataframe['location'] = output_dataframe.apply(lambda row: compute_location(row), axis=1)
    output_dataframe['as_of_date'] = output_dataframe.apply(lambda row: compute_date(row), axis=1)
    return output_dataframe

def generate_csv_using_pandas(output_dataframe):
    output_dataframe.to_csv(f'{os.getcwd()}/combine-csv-data/CSV_combine_task_output.csv', index=False)

def generate_csv_using_Dictfn(output_dataframe):
    dict = output_dataframe.to_dict()
    keys = [key for key in dict]

    for key in keys:
        dict.update({key : list(dict[key].values())})

    with open(f'{os.getcwd()}/combine-csv-data/CSV_combine_task_output.csv', "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(dict.keys())
        writer.writerows(zip(*dict.values()))

if __name__ == '__main__':
    excel_path = f'{os.getcwd()}/combine-csv-data/Excelsheets/'
    output_dataframe = build_dataframe(excel_path)
    generate_csv_using_pandas(output_dataframe)
    # generate_csv_using_Dictfn(output_dataframe)
