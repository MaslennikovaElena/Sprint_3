from selenium.webdriver.common.by import By

from locators import CONSTRUCTOR_BREAD_LINK_XPATH, CONSTRUCTOR_SAUSE_LINK_XPATH, \
    CONSTRUCTOR_FILLING_LINK_XPATH, CONSTRUCTOR_BREAD_HEADER_XPATH, CONSTRUCTOR_SAUSE_HEADER_XPATH, \
    CONSTRUCTOR_FILLING_HEADER_XPATH
from urls import PAGE_MAIN


def test_constructor_to_bread_success(web_driver):
    web_driver.get(PAGE_MAIN)
    # Сперва переходим на другой элемент, иначе текущий не является в начале кликабельным
    web_driver.find_element(By.XPATH, CONSTRUCTOR_SAUSE_LINK_XPATH).click()
    web_driver.find_element(By.XPATH, CONSTRUCTOR_BREAD_LINK_XPATH).click()

    assert web_driver.find_element(By.XPATH, CONSTRUCTOR_BREAD_HEADER_XPATH).is_displayed()


def test_constructor_to_sause_success(web_driver):
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, CONSTRUCTOR_SAUSE_LINK_XPATH).click()

    assert web_driver.find_element(By.XPATH, CONSTRUCTOR_SAUSE_HEADER_XPATH).is_displayed()


def test_constructor_to_filling_success(web_driver):
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, CONSTRUCTOR_FILLING_LINK_XPATH).click()

    assert web_driver.find_element(By.XPATH, CONSTRUCTOR_FILLING_HEADER_XPATH).is_displayed()
