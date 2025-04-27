import pytest
from pages2.login_page2 import LoginPage2
from pages2.dashboard_page_2 import DashboardPage2

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture
def browser():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()

def test_menu_visibility_and_clickable(browser):
    login_page_2 = LoginPage2(browser)
    dashboard_page_2 = DashboardPage2(browser)

    login_page_2.login(USERNAME,PASSWORD)
    dashboard_page_2.verify_menu_items()