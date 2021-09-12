from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    TXT_USERNAME = (By.NAME, "userName")
    TXT_PASSWORD = (By.NAME, "password")
    BTN_SUBMIT = (By.NAME, "submit")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.send_keys(self.TXT_USERNAME, email)
        self.send_keys(self.TXT_PASSWORD, password)
        self.click(self.BTN_SUBMIT)
