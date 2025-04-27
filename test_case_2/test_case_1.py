import pytest
import pickle
import os
from pages2.login_page2 import LoginPage2
from utils.fixture_setup_2 import setup

from utils.data_reader_1 import read_test_file1

EXCEL_FILE = r"D:\project\data_test.xlsx"
SHEET_NAME = "Sheet1"
test_data = read_test_file1(EXCEL_FILE, SHEET_NAME)

@pytest.mark.parametrize("username,password,expected_result", [(data['username'], data['password'], data['Test Result']) for data in test_data])
def test_login(setup, username, password, expected_result):
    driver = setup
    login_page2 = LoginPage2(driver)

    login_page2.enter_username(username)
    login_page2.enter_password(password)
    login_page2.click_login()

    actual_result = "pass" if login_page2.is_logged_in() else "fail"

    if actual_result == "pass":
        with open("cookies/cookies.pkl", "wb") as f:
            pickle.dump(driver.get_cookies(), f)

    assert actual_result == expected_result, f"login test failed for {username}"

def test_login_using_cookies(setup):
    driver = setup
    if os.path.exists("cookies/cookies.pkl"):
        with open("cookies/cookies.pkl", "rb") as f:
            cookies = pickle.load(f)

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()

        login_page2 = LoginPage2(driver)
        assert login_page2.is_logged_in(), "Login failed using cookies"
    else:
        pytest.skip("No cookies available for login")