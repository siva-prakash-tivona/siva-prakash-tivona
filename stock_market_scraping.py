from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import pandas as pd
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.moneycontrol.com/markets/global-indices/')
driver.implicitly_wait(10)
driver.maximize_window()
name = ""
current_value = ""
open_data = ""
high = ""
low = ""
prev_close = ""

def build_data():
    marketdata = []  
    r=1
    element_locator = '//*[@id="mc_content"]/div/div[4]/div/div/div[1]/div/table/tbody'
    while(r <= 16): 
        try:
            name = driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[1]/a').get_attribute('title')
            if driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[2]/div').text:
                current_value = driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[2]/div').text
                open_data = driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[5]').text
                high = driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[6]').text
                low = driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[7]').text
                prev_close = driver.find_element(By.XPATH, f'{element_locator}/tr['+str(r)+']/td[8]').text
            Table_dict={
            'Name' : name,
            'Current Value': current_value,
            'Open' : open_data,
            'High' : high,
            'Low' : low,
            'Prev.Close' : prev_close,
            'Delta' : float("{:.2f}".format(float(current_value.strip().replace(",","")) - float(prev_close.strip().replace(",",""))))
            }
            marketdata.append(Table_dict) 
        except NoSuchElementException as e: 
            print(e)
        r+=1
    return marketdata

def built_csv_with_pandas(marketdata):
    df=pd.DataFrame(marketdata)
    df.to_csv('Stock Market Data.csv') 

def built_csv_with_Dictfn(marketdata):
    keys = marketdata[0].keys()
    with open('Stock Market Data.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(marketdata)

if __name__ == '__main__':
    marketdata = build_data()
    # built_csv_with_pandas(marketdata)
    built_csv_with_Dictfn(marketdata)
    driver.quit()