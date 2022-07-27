from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
import math


pagesIDs = ["236895", '236896', '236897', '236898', '236899', '236903', '236904', '236905']

def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nStarting the browser")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nClosing the browser')
    browser.quit()

@pytest.mark.parametrize('ids', pagesIDs)
def testMultiplePages(browser, ids):
    browser.implicitly_wait(20)
    browser.get(f'https://stepik.org/lesson/{ids}/step/1')

    inputField = browser.find_element(By.TAG_NAME, 'textarea')
    inputField.send_keys(answer())

    submit_button = browser.find_element(By.CLASS_NAME, "submit-submission")
    submit_button.click()
    
    correct_sign = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    
    assert correct_sign == "Correct!", f"Ожидаемый текст отличается от \"Correct\" и равен - {correct_sign}!"
