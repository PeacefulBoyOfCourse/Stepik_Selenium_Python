from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6,
                                        pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = ('http://selenium1py.pythonanywhere.com/catalogue/'
           'coders-at-work_207/?promo=offer{}'.format(promo_code))
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_name_equals_added_to_basket_product()
    product_page.should_be_product_name_price_equals_added_to_basket_product_price()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url)
    product_page.open()  # 1.Открываем страницу товара
    product_page.add_product_to_basket()  # 2.Добавляем товар в корзину
    product_page.should_not_be_success_message()  # 3.Нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url)
    product_page.open()  # 1.Открываем страницу товара
    product_page.should_not_be_success_message()  # 2.Нет сообщения об успехе с помощью is_not_element_present


def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, url)
    product_page.open()  # 1.Открываем страницу товара
    product_page.add_product_to_basket()  # 2.Добавляем товар в корзину
    product_page.should_success_message_disappear()  # 3.Проверяем, что нет сообщения об успехе с помощью is_disappeared


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
