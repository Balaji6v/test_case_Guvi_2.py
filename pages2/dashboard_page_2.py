from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage2:
    MENU_ITEMS = {
        "Admin": "//span[text()='Admin']",
        "PIM": "//span[text()='PIM']",
        "Leave": "//span[text()='Leave']",
        "Time": "//span[text()='Time']",
        "Recruitment": "//span[text()='Recruitment']",
        "My Info": "//span[text()='My Info']",
        "Performance": "//span[text()='Performance']",
        "Dashboard": "//span[text()='Dashboard']",
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_menu_items(self):
        for name, xpath in self.MENU_ITEMS.items():
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            assert element.is_displayed(), f" {name} menu is not visible"
            assert self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))), f"{name} menu is not clickable"

    def is_dashboard_displayed(self):
        try:
            dashboard_header = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            return dashboard_header.is_displayed()
        except:
            return False

    def logout(self):
        try:
            user_dropdown = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab")) )
            user_dropdown.click()
            logout_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
            logout_option.click()
        except Exception as e:
            raise Exception(f"Logout failed: {e}")
