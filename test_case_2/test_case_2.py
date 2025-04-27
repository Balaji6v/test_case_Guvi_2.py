
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.fixture_setup_2 import setup

def test_home_url(setup):
    driver = setup
    home_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(home_url)

    wait = WebDriverWait(driver, 10)
    login_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']")))

    assert driver.current_url == home_url, "Home URL did not load correctly"
    assert login_field.is_displayed(), "Login field is not visible on the home page"