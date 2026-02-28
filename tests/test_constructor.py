import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestConstructor:
    @pytest.mark.parametrize("tab_locator, expected_text", [
        (TestLocators.TAB_SAUCES, "Соусы"),
        (TestLocators.TAB_FILLINGS, "Начинки"),
        (TestLocators.TAB_BUNS, "Булки")
    ], ids=["sauces_tab", "fillings_tab", "buns_tab"])
    
    def test_switch_constructor_tabs(self, driver, tab_locator, expected_text): #Переключение между разделами Булки, Соусы, Начинки
        
        driver.get("https://stellarburgers.education-services.ru")
        # Если проверяем "Булки", сначала кликнем на другой таб (т.к. булки активны сразу)
        if expected_text == "Булки":
            driver.find_element(*TestLocators.TAB_SAUCES).click()
            WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(TestLocators.ACTIVE_TAB, "Соусы"))
        driver.find_element(*tab_locator).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(TestLocators.ACTIVE_TAB, expected_text))
        # Проверяем, что активный таб изменился
        assert expected_text in driver.find_element(*TestLocators.ACTIVE_TAB).text
