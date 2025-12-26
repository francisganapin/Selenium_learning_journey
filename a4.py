from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

try:

    driver.get('https://the-internet.herokuapp.com/dropdown')

    dropdown = driver.find_element(By.ID,'dropdown')

    select = Select(dropdown)

    print('Selecting option 1')
    select.select_by_visible_text('Option 1')
    time.sleep(2)

    print('Selecting option 2')
    select.select_by_visible_text('Option 2')
    time.sleep(10)

    print("Taking screenshot")
    driver.save_screenshot('screenshot.png')

    time.sleep(10)

finally:
    driver.quit()