from selenium.webdriver.common.by import By


class AuthLocators:
    # Локаторы для таба элементов
    LOCATOR_FOR_PHONE=(By.XPATH, '//div[@id="t-btn-tab-phone"]')    # Локатор для таба "Телефон"
    LOCATOR_FOR_EMAIL=(By.XPATH, '//div[@id="t-btn-tab-mail"]')     # Локатор для таба "Почта"
    LOCATOR_FOR_LOGIN=(By.XPATH, '//div[@id="t-btn-tab-login"]')        # Локатор для таба "Логин"
    LOCATOR_FOR_LS=(By.XPATH, '//div[@id="t-btn-tab-ls"]')      # Локатор для таба "Лицевой счет"

    # Локаторы для ввода данных
    LOCATOR_FOR_INPUT_USERNAME = (By.XPATH, '//input[@id="username"]')         # Локатор для ввода "Мобильный телефон"
    LOCATOR_FOR_INPUT_PASS = (By.XPATH, '//input[@id="password"]')      # Локатор для ввода "Пароль"
    LOCATOR_FOR_SING_IN_BUTTON = (By.XPATH, '//button[@id="kc-login"]')        # Локатор для кнопки "Войти"

    LOCATOR_FOR_AUTH = (By.XPATH, '//div[@class="base-card home__info-card"]')
    # Локатор для вывода ошибки при некорректном вводе
    LOCATOR_FOR_ERROR = (By.XPATH, '//span[@id="form-error-message"]')
    # Локатор капчи
    LOCATOR_FOR_CAPTCHA = (By.XPATH, '//div[@class="card-error"]')

    # Локатор для входа по почте или телефону
    LOCATOR_FOR_CODE_BUTTON = (By.XPATH, '//button[@id="back_to_otp_btn"]')
    LOCATOR_FOR_ENTER_DATA = (By.XPATH, '//input[@id="address"]')
    LOCATOR_FOR_CODE_SUBMIT = (By.XPATH, '//button[@id="otp_get_code"]')

    # Локатор для кнопки Забыл пароль
    LOCATOR_FORGOT_PASSWORD = (By.XPATH, '//a[@id="forgot_password"]')
    LOCATOR_FOR_RESET = (By.XPATH, '//button[@id="reset"]')
    LOCATOR_AUTH_BTN = (By.XPATH, '//button[@id="standard_auth_btn"]')

    # Локатор для кода подтверждения
    LOCATOR_CODE = (By.XPATH, '//h1[@class="card-container__title"]')