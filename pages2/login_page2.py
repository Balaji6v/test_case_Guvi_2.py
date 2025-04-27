from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage2:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.XPATH, "//input[@placeholder='Username']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.logout_link = (By.XPATH, "//a[contains(text(),'Logout')]")

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_logged_in(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.logout_link))
            return True
        except:
            return False