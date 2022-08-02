from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_CARD_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADDED_PRODUCT_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    ADDED_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]")
