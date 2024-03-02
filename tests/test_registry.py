from pages.login_in_page import RegistryPage
import time, os, pytest
from dotenv import load_dotenv
from locators.login_in_locators import RegisterLocators as RL

load_dotenv()

name = os.getenv("NAME")
surname = os.getenv("SURNAME")
exist_email = os.getenv("EXIST_EMAIL")
new_email = os.getenv("NEW_USER_MAIL")
password = os.getenv("PASSWORD")
confirm_password = os.getenv("CONFIRM_PASSWORD")
fake_password = os.getenv("INCORRECT_PASSWORD")
phone = os.getenv("PHONE_NUMBER")
wrong_name = os.getenv("INCORRECT_NAME")

"""Тест-кейс для проверки ввода данных"""


@pytest.mark.registation
@pytest.mark.parametrize("name, surname, email, password, confirm_password",
                         [(name, surname, new_email, password, confirm_password),
                          (name, surname, phone, password, confirm_password),
                          (name, surname, exist_email, password, confirm_password),
                          (name, surname, new_email, password, fake_password),
                          (wrong_name, surname, new_email, password, confirm_password)])
def test_reg(driver, name, surname, email, password, confirm_password):
    registry_page = RegistryPage(driver)

    # Так, как url страницы регистрации динамический: переходим на страницу авторизации и кликаем ссылку "Зарегистрироваться"
    registry_page.go_to_reg()
    registry_page.click_button(RL.LOCATOR_FOR_REG)

    # Вводим данные
    registry_page.enter_data(RL.LOCATOR_FOR_NAME, name)
    registry_page.enter_data(RL.LOCATOR_FOR_SURNAME, surname)
    registry_page.enter_data(RL.LOCATOR_FOR_MAIL_OR_PHONE, email)
    registry_page.enter_data(RL.LOCATOR_FOR_PASS, password)
    registry_page.enter_data(RL.LOCATOR_FOR_PASS_CONFIRM, confirm_password)

    # Нажимаем на кнопку регистрации
    registry_page.click_button(RL.LOCATOR_FOR_BUTTON)
    # time.sleep(5)

    if email == new_email or phone:
        assert registry_page.confirm_form(RL.LOCATOR_FOR_END_REG)
        print("Форма для ввода кода успешно открыта")
    # Проверяем, что если почта уже существует, то выводится соответствующее сообщение
    if email == exist_email:
        assert registry_page.confirm_form(RL.LOCATOR_FOR_EXIST_USER)
        print("Выведено сообщение о существующем пользователе")
    # Проверяем, что если пользователь вводит разные пароль и подтверждение пароля, то выводится соответствующее сообщение
    if confirm_password == fake_password:
        assert registry_page.confirm_form(RL.LOCATOR_FOR_ERROR_PASS)
        print("Выведено сообщение о несовпадающем пароле")
    # Проверяем, что если пользователь некорректно введет имя, фамилию, пароль или почту, то всплывет соответствующее сообщение
    if name == wrong_name:
        assert registry_page.confirm_form(RL.LOCATOR_FOR_ERROR_NAME)
        print("Выведено сообщение о некорректном вводе имени")
    # Так, как тег с текстом ошибки у всех полей одинаковый(отличается только текст ошибки) нет необходимости проверять остальные поля на некорректный ввод


"""Тест-кейс проверок ссылки "пользовательского соглашения", кнопок соцсетей и "Помощь" """

# Помещаем локаторы соцсетей в список
all_social = [RL.LOCATOR_FOR_VK_BUTTON, RL.LOCATOR_FOR_OK_BUTTON,
              RL.LOCATOR_FOR_MAIL_BUTTON, RL.LOCATOR_FOR_YA_BUTTON,
              RL.LOCATOR_FOR_LINC, RL.LOCATOR_FOR_HELP]


@pytest.mark.social
@pytest.mark.parametrize("social_locator", all_social)
def test_buttons(driver, social_locator):
    # Переменные
    button = RegistryPage(driver)

    # Переходим на страницу регистрации
    button.go_to_site()

    # Кликаем по кнопке
    button.click_button(social_locator)

    # Подтверждаем, что пользователь оказался на нужной странице после нажатия на кнопку или ссылку
    if social_locator == RL.LOCATOR_FOR_VK_BUTTON:
        assert button.confirm_form(RL.LOCATOR_SUBMIT_VK)

    if social_locator == RL.LOCATOR_FOR_OK_BUTTON:
        assert button.confirm_form(RL.LOCATOR_SUBMIT_OK)

    if social_locator == RL.LOCATOR_FOR_MAIL_BUTTON:
        assert button.confirm_form(RL.LOCATOR_SUBMIT_EMAIL)
    # При нажатии кнопки яндекса
    if social_locator == RL.LOCATOR_FOR_YA_BUTTON:
        assert button.confirm_form(RL.LOCATOR_SUBMIT_YA)

    if social_locator == RL.LOCATOR_FOR_LINC:
        assert button.confirm_form(RL.LOCATOR_FOR_LINC)

    if social_locator == RL.LOCATOR_FOR_HELP:
        assert button.confirm_form(RL.LOCATOR_SUBMIT_HELP)
