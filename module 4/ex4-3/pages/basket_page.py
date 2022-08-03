from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LIST), "Basket is not empty"

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "There is not \"Basket is empty\" text"
