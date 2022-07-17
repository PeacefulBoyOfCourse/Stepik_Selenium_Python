from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

file_path = os.getcwd() + '/' + 'requirements.txt' 

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    firstname.send_keys("Geovanni")

    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys("Georgio")

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys("geovanni_g@google.com")

    file = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
    file.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()