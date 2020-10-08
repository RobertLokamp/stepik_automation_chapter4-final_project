from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    # добавление товара в корзину
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    # проверка, что есть сообщение об успешном добавлении в корзину
    def message_about_product_add_in_basket(self):
        # наличие сообщения
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "There is no message about successfully adding a product to the basket"
        # имя товара в сообщении соответствует имени добавленного товара
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, \
            "The product name in the message differs from the name of the product being added"

    # проверка, что после добавления, в корзине отображается стоимость товара
    def price_of_product_in_basket(self):
        # наличие сообщения
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUM_IN_BASKET), \
            "There is no message with the cost of the product in the basket"
        # стоимость товара в сообщении соответствует стоимости добавленного товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price == product_price_in_message, \
            "The cost of the product in the message differs from the cost of the added product"

    # проверка, что нет сообщения об успешном добавлении в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # # проверка, что не появляется сообщение об успешном добавлении в корзину
    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # расчёт математического выражения
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
