from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    first_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    input_value = browser.find_element(By.ID, "input_value").text
    x = calc(int(input_value))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    submit_button.click()

    print(browser.switch_to.alert.text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()