from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    value_x = treasure.get_attribute("valuex")

    x = calc(value_x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(str(x))

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()