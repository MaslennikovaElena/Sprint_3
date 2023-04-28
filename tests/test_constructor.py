from selenium.webdriver.common.by import By

from locators import ConstructorLocator
from urls import PAGE_MAIN


def test_constructor_to_bread_success(web_driver):
    web_driver.get(PAGE_MAIN)
    # Сперва переходим на другой элемент, иначе текущий не является в начале кликабельным
    web_driver.find_element(By.XPATH, ConstructorLocator.SAUSE_LINK_XPATH).click()
    web_driver.find_element(By.XPATH, ConstructorLocator.BREAD_LINK_XPATH).click()

    bread_header = web_driver.find_element(By.XPATH, ConstructorLocator.BREAD_HEADER_XPATH)
    assert bread_header.is_displayed() and bread_header.text == "Булки"


def test_constructor_to_sause_success(web_driver):
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, ConstructorLocator.SAUSE_LINK_XPATH).click()

    sause_header = web_driver.find_element(By.XPATH, ConstructorLocator.SAUSE_HEADER_XPATH)
    assert sause_header.is_displayed() and sause_header.text == "Соусы"


def test_constructor_to_filling_success(web_driver):
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, ConstructorLocator.FILLING_LINK_XPATH).click()

    fillings_header = web_driver.find_element(By.XPATH, ConstructorLocator.FILLING_HEADER_XPATH)
    assert fillings_header.is_displayed() and fillings_header.text == "Начинки"
