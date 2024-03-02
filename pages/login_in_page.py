from selenium.common import NoSuchElementException
from base_page.base import BasePage


class RegistryPage(BasePage):
    # Метод для нажатия на ссылку регистрации
    def click_button(self, locator):
        element = self.find_element(locator, time=10)
        element.click()
        return element

    def enter_data(self, locator, value):
        element = self.find_element(locator, time=10).send_keys(value)
        return element

    # Методы для парсинга всплывающего окна
    def confirm_form(self, locator):
        try:
            element = self.find_element(locator, time=10)
            return element.is_displayed()  # Если окно с информацией всплывает, то вернется True
        except NoSuchElementException:  # Если окно с информацией не всплывает, то вернется False
            return False
