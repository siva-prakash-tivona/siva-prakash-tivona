# - Scrap table data from this webpage "https://www.aptransport.org/html/registration-statecodes.html"
# - Create a csv file based on the data scrapped from the webpage - 'StatetoAbrivation.csv'
# - Read the initial covid_state_file wherever the state of the covid_state file is matching in the 'StatetoAbrivation.csv'
# - Take the abbrivation and create a new column only if the data is matched
# - Now you take the unique states data and create a unique state_wise data using buildin Csv package

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
import os,pandas as pd, csv
from collections import OrderedDict


driver = webdriver.Chrome()
# driver.get('https://www.aptransport.org/html/registration-statecodes.html')
# driver.implicitly_wait(5)
# driver.maximize_window()

base_folder, file_name = os.path.split(os.path.realpath(__file__))


def generate_states_list(df):
    return df.State.unique()

def generate_statewise_csv(csv):
    df = pd.read_csv(csv)
    states_list = generate_states_list(df)
    for state in states_list:
        if state != 'India':
            state_data = df.loc[df['State'] == state]
            state_data.to_csv(os.path.join(base_folder, 'Output-CSV-using-Pandas',  f'{state}_data.csv'))

def build_state_abbrivation_table():
    print('Starting Scrapping of State Abbrivation Table')
    reg_table_row_locator = '//div[@class="content"]/table/tbody/tr'
    r = 2
    state_code_table = []
    while (1):
        try:
            state_name = driver.find_element(By.XPATH, f'{reg_table_row_locator}[{r}]/td[2]').text
            state_code = driver.find_element(By.XPATH, f'{reg_table_row_locator}[{r}]/td[3]').text
            Table_dict = {
                'State' : state_name,
                'State_code' : state_code
            }
            state_code_table.append(Table_dict)
            r+=1
        except NoSuchElementException as e: 
            print(e)
            break

    keys = state_code_table[0].keys()
    save_csv_using_csv_package(state_code_table, 'StatetoAbbrivation', keys)
    return state_code_table


def combine_and_generate_state_wise_csvs():
    merged_csv = []
    csv_with_state_code = []
    unique_states_data = {}
    input_file1 = csv.DictReader(open(os.path.join(base_folder , 'covid_vaccine_statewise.csv')))
    input_file2 = csv.DictReader(open(os.path.join(base_folder , 'StatetoAbbrivation.csv')))
    # input_file1['Statecode'] = input_file1['State'].map(input_file2['State'])
    # data = list(map(lambda a , b : a if(a['State'] in b['State']) else None, input_file1 , input_file2))
    
    # for state_code in input_file2:
    #     state_data = list(map(lambda x: x if(state_code['State'] in x['State']) else None,input_file1))
    #     print(state_data)

    dat = list(input_file1)
    for data in dat:
        if data['State'] == 'India':
            state_code = [{'State' : '/', 'State_code' : '/'}]
        # elif state_code[0]['State'] in data['State']:
        #     data['State_code'] = state_code[0]['State_code']
        else:
            state_code = []
            # state_code = list(filter(lambda state_abbr: state_abbr['State_code'] if(state_abbr['State'] in data['State']) else None, input_file2))
        # data['State_code'] = state_code[0]['State_code']
            d = list(filter(lambda  y : y['State_code']  if(data['State'] in y['State']) else 'n' ,  input_file2))
        csv_with_state_code.append(data)
    print(data)
    # with open(os.path.join(base_folder , 'covid_vaccine_statewise.csv'), 'r') as f:
    #     for state_wise_data_row in csv.reader(f):
    #         with open(os.path.join(base_folder , 'StatetoAbbrivation.csv'), 'r') as b:
    #             for state_code_data_row in  csv.reader(b):
    #                 if state_wise_data_row[1] == state_code_data_row[0]:
    #                     merged_csv.append(state_wise_data_row+[state_code_data_row[1]])  
    #                     if  state_wise_data_row[1] != 'India':
    #                         if state_wise_data_row[1] not in unique_states_data:
    #                             unique_states_data[state_wise_data_row[1]] = [state_wise_data_row+list(state_code_data_row[1])]
    #                         else:
    #                             unique_states_data[state_wise_data_row[1]].append(state_wise_data_row+[state_code_data_row[1]])
    # merged_csv_keys = merged_csv[0]
    save_csv_using_csv_package(merged_csv, 'State_wise_data_with_Statecode', None)
    key = []
    for state_name, row_data in unique_states_data.items():
        if state_name == 'State':
            key = row_data[0]
            continue
        save_csv_using_csv_package(row_data, f'Output-CSVS_using_csv_package/{state_name}_data', key)


    return merged_csv, unique_states_data

def save_csv_using_csv_package(data_to_save, file_name, keys):
    with open(os.path.join(base_folder , f'{file_name}.csv'), 'w', newline='') as output_file:
        print(type(data_to_save[0]))
        if type(data_to_save[0]) == dict:
            dict_writer = csv.DictWriter(output_file, fieldnames= keys)
            dict_writer.writeheader()
            dict_writer.writerows(data_to_save)
        else :
            csvwriter = csv.writer(output_file) 
            if keys:
                csvwriter.writerow(keys) 
            csvwriter.writerows(data_to_save)

    print(f'Saved {file_name}.csv')


if __name__ == '__main__':
    # csv = f'{os.getcwd()}/Condition-based-pdf-split/covid_vaccine_statewise.csv'
    # generate_statewise_csv(csv)
    # build_state_abbrivation_table()
    merged_csv, unique_states_data = combine_and_generate_state_wise_csvs()
