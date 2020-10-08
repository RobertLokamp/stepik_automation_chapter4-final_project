from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка на корректный url адрес
    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        url_in_browser = self.browser.current_url
        assert "login" in url_in_browser, "'Login' is not in url in browser"

    # проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # проверка, что есть форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(self, email, password):
        email_in_register = self.browser.find_element(*LoginPageLocators.EMAIL_IN_REGISTER)
        email_in_register.send_keys(email)
        password_in_register = self.browser.find_element(*LoginPageLocators.PASSWORD_IN_REGISTER)
        password_in_register.send_keys(password)
        repeat_password_in_register = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_IN_REGISTER)
        repeat_password_in_register.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()




