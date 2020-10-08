from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# неавторизованный пользователь может перейти на страницу логина/регистрации
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # переход между страницами
    login_page.should_be_login_page()  # проверка содержимого страницы логина/регистрации


# у неавторизованного пользователя пустая корзина при переходе в неё из шапки
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()  # открытие страницы корзины
    page.basket_is_empty_message()  # есть сообщение о том, что корзина пуста
    page.basket_is_empty_quantity()  # не отображается количество товаров в пустой корзине


# неавторизованный пользователь видит ссылку на страницу логина/регистрации
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # есть ссылка на страницу логина/регистрации
