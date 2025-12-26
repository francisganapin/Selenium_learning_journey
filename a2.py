from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

try:
    driver.get('https://www.python.org')

    # 1 find The search box by it's name "q"
    search_box = driver.find_element(By.NAME, "q")
    
    # 2. Type pycon and press Enter
    print("Search for 'pycon'...")
    search_box.send_keys('pycon')
    search_box.send_keys(Keys.RETURN)


    # 3. Verify we are on the results page
    assert "Python.org" in driver.title
    print('Search successful!')
    time.sleep(5)

finally:
    driver.quit()