import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestNavigation:
    def test_open_profile_page(self, logged_in_driver): # Переход в Личный Кабинет авторизованным пользователем
        
        logged_in_driver.find_element(*TestLocators.HEADER_PROFILE_LINK).click()
        WebDriverWait(logged_in_driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in logged_in_driver.current_url

    @pytest.mark.parametrize("nav_element", 
                            [TestLocators.HEADER_CONSTRUCTOR_LINK, TestLocators.HEADER_LOGO],
                            ids=["constructor_text", "stellar_logo"])
    def test_back_to_constructor_from_profile(self, logged_in_driver, nav_element): # Переход из профиля обратно в Конструктор через логотип или текст
       
        logged_in_driver.find_element(*TestLocators.HEADER_PROFILE_LINK).click()
        logged_in_driver.find_element(*nav_element).click()
        title = WebDriverWait(logged_in_driver, 10).until(EC.visibility_of_element_located(TestLocators.MAIN_CONSTRUCTOR_TITLE))
        assert title.is_displayed()
