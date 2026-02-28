import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestLogout:
    def test_logout_success(self, logged_in_driver): # Выход из аккаунта через кнопку в Личном Кабинете
        
        logged_in_driver.find_element(*TestLocators.HEADER_PROFILE_LINK).click()
        exit_btn = WebDriverWait(logged_in_driver, 10).until(EC.element_to_be_clickable(TestLocators.PROFILE_EXIT_BUTTON))
        exit_btn.click()
        WebDriverWait(logged_in_driver, 10).until(EC.url_contains("/login"))
        assert "/login" in logged_in_driver.current_url
