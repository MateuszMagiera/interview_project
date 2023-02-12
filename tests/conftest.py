import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='function')
def setUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    chrome_options =webdriver.ChromeOptions()
##  Uncomment the following line in order to run tests in the headless mode (currently works only for the chrome browser)
    # chrome_options.add_argument("--headless")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    elif browser_name == 'firefox':
         driver = webdriver.Firefox()
    driver.get("https://staging.app.zaplify.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
