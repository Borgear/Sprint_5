import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestLogin:
    
    @pytest.mark.parametrize("start_url, button_to_click", [
        ("https://stellarburgers.education-services.ru", TestLocators.MAIN_LOGIN_BUTTON),
        ("https://stellarburgers.education-services.ru", TestLocators.HEADER_PROFILE_LINK),
        ("https://stellarburgers.education-services.ru/register", TestLocators.REG_LOGIN_LINK),
        ("https://stellarburgers.education-services.ru/forgot-password", TestLocators.FORGOT_LOGIN_LINK)],
        ids=["from_main_page", "from_header_profile", "from_reg_form", "from_forgot_pass"])
    
    def test_login(self, driver, created_user, start_url, button_to_click): #Тесты входа с использованием заранее созданного пользователя
                
        email, password = created_user
        driver.get(start_url)
        driver.find_element(*button_to_click).click()
        # Заполнение формы авторизации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.LOGIN_EMAIL_INPUT))
        driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.LOGIN_SUBMIT_BUTTON).click()
        # Проверяем успешный вход
        order_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TestLocators.MAIN_ORDER_BUTTON)
        )
        assert order_btn.is_displayed()
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
