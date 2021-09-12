import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def init_driver(request):
    """Set Up"""
    global web_driver

    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL)

    """Tear Down"""
    yield
    web_driver.quit()
