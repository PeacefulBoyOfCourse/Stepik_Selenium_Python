from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.ID, "button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()