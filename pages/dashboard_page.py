from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage(BasePage):
    # Top navigation menu locators
    SERVICES_MENU = (By.XPATH, "//span[normalize-space()='Services']")
    CATEGORIES_OPTION = (By.XPATH, "//span[normalize-space()='Categories']") # Dropdown er option

    def __init__(self, driver):
        super().__init__(driver)

    def is_dashboard_loaded(self):
        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: "home" in driver.current_url.lower()
            )
            return True
        except:
            return False

    def hover_on_services(self):
        # Services menu-r opor mouse cursor (hover) korbe jate dropdown ashe
        services_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SERVICES_MENU)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(services_element).perform()

    def click_categories_from_dropdown(self):
        # Dropdown menu theke 'Categories'-e click korbe
        categories_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CATEGORIES_OPTION)
        )
        categories_element.click()