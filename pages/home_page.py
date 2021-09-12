from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LBL_LOGIN_SUCCESS = (By.XPATH, "//h3")
    LINK_SIGN_OFF = (By.XPATH, "//a[text()='SIGN-OFF']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_logged_in_success_message(self):
        return self.get_element_text(self.LBL_LOGIN_SUCCESS)

    def sign_off(self):
        self.click(self.LINK_SIGN_OFF)
