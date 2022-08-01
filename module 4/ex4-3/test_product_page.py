from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, 
                        pytest.param("7", marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    url = ('http://selenium1py.pythonanywhere.com/catalogue/'
                   'coders-at-work_207/?promo=offer{}'.format(promo_code))
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_name_equals_added_to_basket_product()
    product_page.should_be_product_name_price_equals_added_to_basket_product_price()
