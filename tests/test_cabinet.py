from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainLocator, CabinetLocator
from urls import PAGE_MAIN, PAGE_LOGIN, PAGE_CABINET


def test_to_cabinet_link_go_cabinet(authorized):
    web_driver = authorized
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, MainLocator.CABINET_BTN_XPATH).click()
    assert web_driver.current_url == PAGE_CABINET


def test_cabinet_constructor_link_go_constructor(authorized):
    web_driver = authorized
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, MainLocator.CABINET_BTN_XPATH).click()
    WebDriverWait(web_driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CabinetLocator.LOGOUT_BTN_XPATH))
    )
    web_driver.find_element(By.XPATH, CabinetLocator.CONSTRUCTOR_BTN_XPATH).click()
    assert web_driver.current_url == PAGE_MAIN


def test_cabinet_logo_click_go_constructor(authorized):
    web_driver = authorized
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, MainLocator.CABINET_BTN_XPATH).click()
    WebDriverWait(web_driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CabinetLocator.LOGOUT_BTN_XPATH))
    )
    web_driver.find_element(By.XPATH, CabinetLocator.SITE_LOGO_XPATH).click()
    assert web_driver.current_url == PAGE_MAIN


def test_cabinet_logout_success(authorized):
    web_driver = authorized
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, MainLocator.CABINET_BTN_XPATH).click()
    WebDriverWait(web_driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CabinetLocator.LOGOUT_BTN_XPATH))
    )
    web_driver.find_element(By.XPATH, CabinetLocator.LOGOUT_BTN_XPATH).click()
    WebDriverWait(web_driver, 10).until_not(
        expected_conditions.visibility_of_element_located((By.XPATH, CabinetLocator.LOGOUT_BTN_XPATH))
    )
    assert web_driver.current_url == PAGE_LOGIN

