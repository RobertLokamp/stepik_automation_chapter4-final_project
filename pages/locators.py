from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#id_login-redirect_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCES_MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    MESSAGE_SUM_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p:nth-child(1)")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
