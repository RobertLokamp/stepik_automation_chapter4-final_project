from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url() #проверка на корректный url адрес
        self.should_be_login_form() #проверка, что есть форма логина
        self.should_be_register_form() #проверка, что есть форма регистрации

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        url_in_browser = self.driver.current_url
        assert "login" in url_in_browser, "'Login' is not in url in browser"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"