from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.admin_tab = (By.XPATH, "//span[text()='Admin']")
        self.add_button = (By.XPATH, "//button[contains(., 'Add')]")
        self.user_role_dropdown = (By.XPATH, "//label[text()='User Role']/../following-sibling::div")
        self.user_role_ess = (By.XPATH, "//div[@role='listbox']//span[text()='ESS']")
        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.username_input = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
        self.status_dropdown = (By.XPATH, "//label[text()='Status']/../following-sibling::div")
        self.status_enabled = (By.XPATH, "//div[@role='listbox']//span[text()='Enabled']")
        self.password_input = (By.XPATH, "//label[text()='Password']/../following-sibling::div//input")
        self.confirm_password_input = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div//input")
        self.save_button = (By.XPATH, "//button[@type='submit' and contains(., 'Save')]")
        self.success_toast = (By.XPATH, "//div[contains(@class,'oxd-toast-content') and contains(., 'Successfully Saved')]")

    def open_admin_tab(self):
        admin = self.wait.until(EC.element_to_be_clickable(self.admin_tab))
        self.driver.execute_script("arguments[0].scrollIntoView();", admin)
        admin.click()

    def add_user(self, emp_name, username, password):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        self.wait.until(EC.presence_of_element_located(self.user_role_dropdown)).click()
        self.wait.until(EC.presence_of_element_located(self.user_role_ess)).click()

        emp_input = self.wait.until(EC.presence_of_element_located(self.employee_name_input))
        emp_input.send_keys(emp_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{emp_name}')]"))).click()

        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)

        self.wait.until(EC.presence_of_element_located(self.status_dropdown)).click()
        self.wait.until(EC.presence_of_element_located(self.status_enabled)).click()

        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.presence_of_element_located(self.confirm_password_input)).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def verify_success(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_toast))

    def search_user(self, username):
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                       "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]/following-sibling::div//input")))
        search_input.clear()
        search_input.send_keys(username)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def is_user_listed(self, username):
        try:
            user = self.wait.until(EC.visibility_of_element_located((By.XPATH,f"//div[@class='oxd-table-body']//div[text()='{username}']")))
            return user.is_displayed()
        except:
            return False