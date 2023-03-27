import os
import time
import logging
import argparse
from dotenv import load_dotenv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape(type: int = 1, date: int = 1):
    """ Scrapes data from SGX website
    
    Args:
        type (int, optional): Desired type to scrape. Defaults to 1.
            1: WEBPXTICK_DT-*.zip
            2: TickData_structure.dat
            3: TC_*.txt
            4: TC_structure.dat
            
        date (int, optional): Desired date to scrape . Defaults to 1.
            1: Newest day
            2: 1 day before
            3: 2 days before
            4: 3 days before
    """
    def selectTypeOfData(type: int = 1):
        while True:
            options = driver.find_elements(By.XPATH, "//*[@id='page-container']/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[1]/label/span[2]/span")
            if len(options) > 0:
                break
            else:
                print('Waiting for element to appear')
                time.sleep(1)
        options[0].click()

        while True:
            options = driver.find_elements(By.XPATH, f"//*[@id='sgx-select-dialog']/div[2]/sgx-select-picker/sgx-list/div/div/sgx-select-picker-option[{type}]/label/span")
            if len(options) > 0:
                break
            else:
                print('Waiting for element to appear')
                time.sleep(1)
        file_name = options[0].text
        options[0].click()
        return file_name

    def selectDate(date: int = 1):
        while True:
            options = driver.find_elements(By.XPATH, "//*[@id='page-container']/template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/sgx-input-select[2]/label/span[2]/span")
            if len(options) > 0:
                break
            else:
                print('Waiting for element to appear')
                time.sleep(1)
        options[0].click()

        while True:
            options = driver.find_elements(By.XPATH, f"//*[@id='sgx-select-dialog']/div[2]/sgx-select-picker/sgx-list/div/div/sgx-select-picker-option[{date}]/label/span")
            if len(options) > 0:
                break
            else:
                print('Waiting for element to appear')
                time.sleep(1)
        file_date = options[0].text
        options[0].click()
        return file_date
        
    def clickDownload(file_name: str = 'Unknown', file_date: str = 'Unknown'):
        while True:
            downloadBtn = driver.find_elements(By.XPATH, "//*[@id='page-container']//template-base/div/div/section[1]/div/sgx-widgets-wrapper/widget-research-and-reports-download[1]/widget-reports-derivatives-tick-and-trade-cancellation/div/button")
            if len(downloadBtn) > 0:
                break
            elif len(downloadBtn) == 0:
                print('Waiting for element to appear')
                time.sleep(1)
            else:
                logging.error('No such file or directory')
        downloadBtn[0].click()
        logging.info(f'Download files {file_name} - {file_date} successfully')

    _file_name = str(selectTypeOfData(type))
    _file_date = str(selectDate(date))
    clickDownload(file_name = _file_name, file_date = _file_date)


def createParser():
    """ Creates parser for CLI usage

    Returns:
        Namespace: input arguments from CLI
    """
    parser = argparse.ArgumentParser(
                prog='Scraper',
                description='Download files from SGX website')
    parser.add_argument('-t', '--type', type=int, nargs='?', default=1, help='Desired type to scrape. Defaults to 1. 1: WEBPXTICK_DT-*.zip 2: TickData_structure.dat 3: TC_*.txt 4: TC_structure.dat')
    parser.add_argument('-d', '--date', type=int, nargs='?', default=1, help='Desired date to scrape . Defaults to 1. 1: Newest day 2: 1 day before 3: 2 days before 4: 3 days before')
    return parser.parse_args()

if __name__ == "__main__":
    
    # Parse arguments
    args = createParser()
    
    # Open webdriver
    load_dotenv(dotenv_path=Path('.env'))
    BASE_URL = os.getenv('BASE_URL')
    driver = webdriver.Edge()
    driver.get(BASE_URL)
    
    # Set logging
    logging.basicConfig(filename='scrape.log', level=logging.INFO, filemode='a', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s')
    
    # Scrape files
    scrape(args.type, args.date)
    
    # Quit webdriver
    time.sleep(5) # for download to complete
    driver.quit()