from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:

    driver.get('https://the-internet.herokuapp.com/login')

    driver.find_element(By.ID,'username').send_keys('tomsmith')

    driver.find_element(By.ID,'password').send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR,'button').click()

    success_message = driver.find_element(By.ID,"flash").text
    print(f"Message Received: {success_message}")

    assert "You logged into a secure area!" in success_message

    print('Login Test Passed!')

    time.sleep(3)

finally:
    driver.quit()