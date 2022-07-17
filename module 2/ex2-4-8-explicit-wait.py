from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    input_value = browser.find_element(By.ID, "input_value").text
    x = calc(int(input_value))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(x)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
