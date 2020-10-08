from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    # прекондишны (регистрация нового пользователя)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "vBR9zbJDbfdvueL"
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)  # регистрация нового пользователя
        login_page.should_be_authorized_user()  # пользователь авторизован

    @pytest.mark.need_review
    # авторизованный пользователь может добавить товар в корзину
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()  # добавление товара в корзину
        page.solve_quiz_and_get_code()  # расчёт математического выражения
        page.message_about_product_add_in_basket()  # есть сообщение об успешном добавлении в корзину
        page.price_of_product_in_basket()  # после добавления, в корзине отображается стоимость товара

    # авторизованный пользователь не видит сообщение об успешном добавлении товара в корзину
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()  # нет сообщения об успешном добавлении в корзину


@pytest.mark.need_review
# неавторизованный пользователь может добавить товар в корзину
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # добавление товара в корзину
    page.solve_quiz_and_get_code()  # расчёт математического выражения
    page.message_about_product_add_in_basket()  # есть сообщение об успешном добавлении в корзину
    page.price_of_product_in_basket()  # после добавления, в корзине отображается стоимость товара


@pytest.mark.need_review
# неавторизованный пользователь может перейти на страницу логина/регистрации со страницы товара
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()  # переход на страницу логина/регистрации


@pytest.mark.need_review
# неавторизованный пользователь не видит товар в корзине после перехода со страницы товара по кнопке из шапки
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()  # открытие страницы корзины
    page.basket_is_empty_message()  # есть сообщение о том, что корзина пуста
    page.basket_is_empty_quantity()  # не отображается количество товаров в пустой корзине


# неавторизованный пользователь не видит соответствующее сообщение об успешном добавлении товара в корзину
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # нет сообщения об успешном добавлении в корзину


@pytest.mark.xfail
# неавторизованный пользователь после добавления товара в корзину не видит соответствующее сообщение об успешном
# добавлении товара
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # добавление товара в корзину
    page.should_not_be_success_message()  # нет сообщения об успешном добавлении в корзину


# неавторизованный пользователь видит ссылку на страницу логина/регистрации на странице товара
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()  # есть ссылка на страницу логина/регистрации


@pytest.mark.xfail
# сообщение об успешном добавлении товара в корзину не появляется через некоторое время
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # добавление товара в корзину
    page.should_not_be_success_message_disappeared()  # не появляется сообщение об успешном добавлении в корзину
