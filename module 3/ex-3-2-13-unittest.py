from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestClass(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name_field.send_keys("Имя")

        second_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        second_name_field.send_keys("Фамилия")

        email_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_field.send_keys("Почтовый адрес")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name_field.send_keys("Имя")

        second_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        second_name_field.send_keys("Фамилия")

        email_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_field.send_keys("Почтовый адрес")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()