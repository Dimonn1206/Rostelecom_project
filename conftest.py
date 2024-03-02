import pytest
import selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=ChromeDriverManager().install())
chrome_options = selenium.webdriver.ChromeOptions


@pytest.fixture(scope="function", autouse=True)
def driver():
    service = selenium.webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=service)
    options = Options()
    options.add_argument("--no-sandbox")
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()
