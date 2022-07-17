from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element(By.ID, "input_value").text
    x = calc(int(value_x))

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 150);")

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(x)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()
    
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()