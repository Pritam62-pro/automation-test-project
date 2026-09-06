from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Login page-er email ar password box-er locator
    EMAIL_INPUT = (By.NAME, "email")       # Jodi id thake tahole (By.ID, "email") dite paro
    PASSWORD_INPUT = (By.NAME, "password") # Jodi id thake tahole (By.ID, "password") dite paro
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)