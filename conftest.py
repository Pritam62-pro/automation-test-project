import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        # GitHub server e display nei, tai headless mode lagbe
        chrome_options.add_argument('--headless') 
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--headless') # Firefox er jonno headless
        
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        
    else:
        raise ValueError(f"Browser {browser_name} not supported")
        
    driver.maximize_window()
    yield driver  # Ekhane test run hobe
    driver.quit() # Test sesh hole browser bondho hoye jabe