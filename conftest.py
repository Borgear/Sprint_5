import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from generator import *

@pytest.fixture
def driver(): # Инициализация браузера перед тестом и закрытие после
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def created_user(driver): # Предварительная регистрация пользователя. Создает аккаунт и возвращает (email, password).
        
    email = generate_unique_email()
    password = generate_random_password(8)
    name = "Dmitry"
    # Регистрация
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys(name)
    driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestLocators.REG_REGISTER_BUTTON).click()
    # Ждем подтверждения регистрации (переход на логин)
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    # Возвращаем данные для входа в тест
    return email, password

@pytest.fixture
def logged_in_driver(driver, created_user): # Вход.

    email, password = created_user 
    # Авторизация
    driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
    # Подтверждаем успешный вход появлением кнопки заказа
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.MAIN_ORDER_BUTTON))
    # Возвращаем драйвер в состоянии "уже залогинен"
    return driver
