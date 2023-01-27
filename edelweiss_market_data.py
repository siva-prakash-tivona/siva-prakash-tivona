from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import pandas as pd
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.edelweiss.in/oyo/equity/top-long-term-stock-recommendations/')
driver.implicitly_wait(10)
driver.maximize_window()

def build_data():
    print('Started Generating Market data')
    marketdata = []  
    r = 0
    midcap_stocks_locator = '//*[@id="activetraderpage"]/div[2]/div[1]/ul/li[2]/a'
    midcap_stocks = driver.find_element(By.XPATH, f'{midcap_stocks_locator}')
    driver.execute_script("arguments[0].click();", midcap_stocks)
    while(1):
        reco_date_locator = f'//*[@id="scheme{r}"]/div[1]/div[1]/label[1]'
        stock_locator = f'//*[@id="scheme{r}"]/div[1]/div[2]/a/label[1]'
        current_price_locator = f'//*[@id="scheme{r}"]/div[1]/label[1]/label[1]/label'
        target_price_locator = f'//*[@id="scheme{r}"]/div[1]/label[2]/label/label'
        market_cap_locator = f'//*[@id="scheme{r}"]/div[1]/label[4]/label[1]'
        sector_locator = f'//*[@id="scheme{r}"]/div[1]/label[5]/label'
        try:
            reco_date = driver.find_element(By.XPATH, reco_date_locator).text.splitlines()
            reco_date_split = reco_date[0].split()
            formatted_reco_date = f'{reco_date_split[2]} {reco_date_split[1]} {reco_date_split[0]}'
            stock = driver.find_element(By.XPATH, stock_locator).text
            current_price = driver.find_element(By.XPATH, current_price_locator).text.replace(',','')
            target_price = driver.find_element(By.XPATH, target_price_locator).text.replace(',','')
            market_cap = driver.find_element(By.XPATH, market_cap_locator).text.replace(',','')
            sector = driver.find_element(By.XPATH, sector_locator).text.replace('\n','')
            Table_dict={
            'Reco Date' : formatted_reco_date,
            'Stock': stock,
            'Current Price' : float(current_price),
            'Target Price' : target_price,
            'Market Cap' : int(market_cap),
            'Sector' : sector
            }
            marketdata.append(Table_dict) 
            r+=1
        except NoSuchElementException as e: 
            print(e)
            break
    print('Generated Market Data')
    return marketdata

def built_csv_with_pandas(marketdata):
    print('Saving Data to CSV using Pandas')
    df=pd.DataFrame(marketdata)
    df.to_csv('Stock Market Data.csv') 
    print('Data written successfully')

def built_csv_with_Dictfn(marketdata):
    print('Saving Data to CSV using Dict function')
    keys = marketdata[0].keys()
    with open('Stock Market Data.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(marketdata)
    print('Data written successfully')
if __name__ == '__main__':
    marketdata = build_data()
        # built_csv_with_pandas(marketdata)
    built_csv_with_Dictfn(marketdata)
    driver.quit()