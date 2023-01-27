from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException

from airflow.operators.selenium_plugin import SeleniumOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
 
def _selenium_task_1():
    

with DAG('selenium_task_combine_dag', start_date=datetime(2022, 1, 1), schedule_interval='@daily', catchup=False) as dag:
    selenium_task_1 = PythonOperator(
        task_id = 'selenium_task_1',
        python_callable=_selenium_task_1
    )

    # selenium_task_2 = PythonOperator(
    #     task_id = 'selenium_task_2',
    #     python_callable=_selenium_task_2
    # )