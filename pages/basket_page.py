from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # проверка, что есть сообщение о том, что корзина пуста
    def basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "There is no message that the basket is empty"

    # проверка, что не отображается количество товаров в пустой корзине
    def basket_is_empty_quantity(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY_QUANTITY), \
            "There are products in the basket"
