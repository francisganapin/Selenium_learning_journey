from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    print('Navigating to Python.org...')
    driver.get('https://www.python.org')

    print(f"Page title is: {driver.title}")
    assert "Python" in driver.title

    time.sleep(5)

finally:

    print('Closing browser....')
    driver.quit()