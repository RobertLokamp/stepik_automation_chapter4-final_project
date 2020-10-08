from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
        "Нет сообщения о том, что корзина пуста"

    def basket_is_empty_quantity(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_QUANTITY), \
        "В корзине есть товары"



