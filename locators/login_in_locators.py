from selenium.webdriver.common.by import By


class RegisterLocators:
    # Локаторы для ввода данных
    LOCATOR_FOR_REG = (By.XPATH, '//a[@id="kc-register"]')
    LOCATOR_FOR_NAME = (By.XPATH, '//input[@name="firstName"]')
    LOCATOR_FOR_SURNAME = (By.XPATH, '//input[@name="lastName"]')
    LOCATOR_FOR_MAIL_OR_PHONE = (By.XPATH, '//input[@id="address"]')
    LOCATOR_FOR_PASS = (By.XPATH, '//input[@id="password"]')
    LOCATOR_FOR_PASS_CONFIRM = (By.XPATH, '//input[@id="password-confirm"]')
    LOCATOR_FOR_BUTTON = (By.XPATH, '//button[@type="submit"]')

    # Локатор для вплывающего сообщения о получении кода по почте или телефону
    LOCATOR_FOR_END_REG = (By.XPATH, '//div[@class="card-container__wrapper"]')

    # Локаторы для всплывающего сообщения, где указано, что почта или телефон уже зарегистрированы
    LOCATOR_FOR_EXIST_USER = (By.XPATH, '//h1[@class="card-container__title"]')

    # Локаторы для вывода сообщений о некорректном вводе
    LOCATOR_FOR_ERROR_PASS = (By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')
    LOCATOR_FOR_ERROR_NAME = (By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

    # Локаторы кнопок в нижней части формы регистрации
    LOCATOR_FOR_LINC = (By.XPATH, '//a[@id="rt-auth-agreement-link"]')
    LOCATOR_FOR_HELP = (By.XPATH, '//a[@class="rt-link rt-link--orange faq-modal-tip__btn"]')
    LOCATOR_FOR_VK_BUTTON = (By.XPATH, '//a[@id="oidc_vk"]')
    LOCATOR_FOR_OK_BUTTON = (By.XPATH, '//a[@id="oidc_ok"]')
    LOCATOR_FOR_MAIL_BUTTON = (By.XPATH, '//a[@id="oidc_mail"]')
    LOCATOR_FOR_YA_BUTTON = (By.XPATH, '//a[@id="oidc_ya"]')

    # Локаторы страниц соцсетей для проверки
    LOCATOR_SUBMIT_VK = (By.XPATH, '//div[@id="root"]')
    LOCATOR_SUBMIT_OK = (By.XPATH, '//div[@id="hook_Block_OAuth2Login"]')
    LOCATOR_SUBMIT_EMAIL = (By.XPATH, '//div[@id="wrp"]')
    LOCATOR_SUBMIT_YA = (By.XPATH, '//div[@class="passp-auth-content"]')
    LOCATOR_SUBMIT_LINC = (By.XPATH, '//div[@id="title"]')
    LOCATOR_SUBMIT_HELP = (By.XPATH, '//header[@id="app-header"]')
