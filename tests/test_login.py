from config.config import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, init_driver):
        global login_page, home_page

        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)

        home_page = HomePage(self.driver)
        assert home_page.get_logged_in_success_message() == "Login Successfully"

    def test_invalid_login(self, init_driver):
        global login_page

        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, "admin123")

        assert login_page.get_page_title() == TestData.LOGIN_PAGE_TITLE
