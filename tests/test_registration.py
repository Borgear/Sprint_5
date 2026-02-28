import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from generator import *

class TestRegistration:
    def test_registration_success(self, driver): # Успешная регистрация с валидными данными
        
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys("Dmitry")
        driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys(generate_random_password(8))
        driver.find_element(*TestLocators.REG_REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_registration_short_password_error(self, driver): # Ошибка при вводе пароля меньше 6 символов
        
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*TestLocators.REG_NAME_INPUT).send_keys("Dmitry")
        driver.find_element(*TestLocators.REG_EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT).send_keys(generate_random_password(5))
        driver.find_element(*TestLocators.REG_REGISTER_BUTTON).click()
        assert driver.find_element(*TestLocators.REG_PASSWORD_ERROR).text == "Некорректный пароль"
