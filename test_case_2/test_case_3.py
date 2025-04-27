from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.fixture_setup_2 import setup

USERNAME_FIELD = (By.NAME, "username")
PASSWORD_FIELD = (By.NAME, "password")

def test_login_fields_visible(setup):
    wait = WebDriverWait(setup, 10)

    username = wait.until(EC.presence_of_element_located(USERNAME_FIELD))
    password = wait.until(EC.presence_of_element_located(PASSWORD_FIELD))

    assert username.is_displayed(), "Username field is not visible"
    assert password.is_displayed(), "Password field is not visible"