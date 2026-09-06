import pytest
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.usefixtures("driver")
class TestClearCutConsole:
    
    def test_hover_and_click_categories(self, driver):
        # 1. Login URL open korchi
        driver.get("https://dev.console.clearrcut.com/")
        
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        
        # 2. Login korchi
        login_page.login("pritambiswas1072@gmail.com", "12345678")
        
        # 3. Dashboard load hoyeche kina check korchi
        assert dashboard_page.is_dashboard_loaded(), "Login fail koreche ba Dashboard load hoyni!"
        
        # 4. Login hoar pore ektu wait korchi
        time.sleep(3)
        
        # 5. Services menu-r opor mouse hover korchi (jate dropdown ashe)
        dashboard_page.hover_on_services()
        time.sleep(2) # Dropdown dekhar jonno choto wait
        
        # 6. Dropdown theke 'Categories'-e click korchi
        dashboard_page.click_categories_from_dropdown()
        time.sleep(3)