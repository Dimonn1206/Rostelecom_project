from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:



    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://b2c.passport.rt.ru"
        self.reg_url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=d7805034-c778-4131-873e-ea85677820c7&theme&auth_type"
        self.code_url = "https://start.rt.ru/"
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_reg(self):
        return self.driver.get(self.reg_url)

    def auth_by_code_site(self):
        return self.driver.get(self.code_url)