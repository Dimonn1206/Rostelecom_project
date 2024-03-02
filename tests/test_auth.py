from pages.auth_page import AuthPage
import time, os, pytest
from locators.auth_locators import AuthLocators as AL
from dotenv import load_dotenv

load_dotenv()

phone = os.getenv("PHONE_NUMBER")
login_password = os.getenv("LOGIN_PASSWORD")
exist_email = os.getenv("EXIST_EMAIL")
ls = os.getenv("LS")
login = os.getenv("LOGIN")
wrong_pass = os.getenv("INCORRECT_PASSWORD")
wrong_mail = os.getenv("NEW_USER_MAIL")

# Создаю кортежи для разных сценарием входа
locators_for_choice = [
    (AL.LOCATOR_FOR_PHONE, phone, login_password),
    (AL.LOCATOR_FOR_LOGIN, login, login_password),
    (AL.LOCATOR_FOR_EMAIL, exist_email, login_password),
    (AL.LOCATOR_FOR_LS, ls, login_password),
    (AL.LOCATOR_FOR_LS, ls, wrong_pass)]

"""Тест-кейс авторизации. Здесь пять сценариев авторизации:
1. Вход по телефону
2. Вход по логину
3. Вход по почте
4. Вход по лицевому счету
5. Вход с некорректными данными"""

@pytest.mark.login
@pytest.mark.parametrize('choice_element, username, password', locators_for_choice)
def test_auth_by_password(driver, choice_element, username, password):
    auth_field = AuthPage(driver)

    auth_field.go_to_site()
    # Выполняем сценарий входа
    auth_field.click_button(choice_element)

    # Вводим данные в поля телефона/почты/личного счета/логина и пароля
    auth_field.enter_data(AL.LOCATOR_FOR_INPUT_USERNAME, username)
    auth_field.enter_data(AL.LOCATOR_FOR_INPUT_PASS, password)

    auth_field.click_button(AL.LOCATOR_FOR_SING_IN_BUTTON)
    # Если пароль верный пользователь проходит авторизацию
    if password == login_password:
        assert auth_field.confirm_form(AL.LOCATOR_FOR_AUTH)
        print("Авторизация прошла успешно")
    # Если пароль не верный ожидается сообщение об ошибке
    if password != login_password:
        assert auth_field.confirm_form(AL.LOCATOR_FOR_ERROR)
        print("Неверные логин или пароль")



"""Тест-кейс авторизации для отправки временного кода"""

data = [(AL.LOCATOR_FOR_ENTER_DATA, phone), (AL.LOCATOR_FOR_ENTER_DATA, exist_email)]

@pytest.mark.login_by_code
@pytest.mark.parametrize('locator, value', data)
def test_auth_by_code(driver, locator, value):
    auth = AuthPage(driver)
    auth.auth_by_code_site()
    # time.sleep(3)
    auth.enter_data(AL.LOCATOR_FOR_ENTER_DATA, value)

    auth.click_button(AL.LOCATOR_FOR_CODE_SUBMIT)
    assert auth.confirm_form(AL.LOCATOR_CODE)
    print("Форма для ввода кода открыта")



"""Тест-кейс восстановления пароля"""
# Создаю кортежи для сценариев восстановления пароля
locators_for_recovery = [
    (AL.LOCATOR_FOR_PHONE, phone),
    (AL.LOCATOR_FOR_LOGIN, login),
    (AL.LOCATOR_FOR_EMAIL, exist_email),
    (AL.LOCATOR_FOR_EMAIL, wrong_mail),
]

@pytest.mark.reset_pass
@pytest.mark.parametrize('choice_element, username', locators_for_recovery)
def test_forgot_password(driver, choice_element, username):
    auth = AuthPage(driver)
    auth.go_to_site()

    auth.click_button(AL.LOCATOR_FORGOT_PASSWORD)

    auth.click_button(choice_element)
    auth.enter_data(AL.LOCATOR_FOR_INPUT_USERNAME, username)
    # time.sleep(5)
    auth.click_button(AL.LOCATOR_FOR_RESET)
    assert auth.confirm_form(AL.LOCATOR_CODE)
    print("Открыта форма восстановления пароля по почте или по номеру телефона")

