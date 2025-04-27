import pytest
from selenium import webdriver
from pages2.login_page2 import LoginPage2
from pages2.admin_page_2 import AdminPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_verify_user_exists(driver):
    login = LoginPage2(driver)
    admin = AdminPage(driver)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")

    admin.open_admin_tab()
    admin.search_user("jane2115")

    assert admin.is_user_listed("jane2115"), "User 'jane2115' not found."