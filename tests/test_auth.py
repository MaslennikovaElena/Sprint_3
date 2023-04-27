from selenium.webdriver.common.by import By

from locators import PAGE_LOGIN, PAGE_MAIN, PAGE_REGISTER, PAGE_REMIND_PWD, MAIN_AUTH_BTN_XPATH, \
    MAIN_CABINET_BTN_XPATH, REGISTER_LOGIN_LINK_XPATH, REMIND_PWD_LOGIN_LINK_XPATH


def test_main_page_auth_btn_success(web_driver):
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, MAIN_AUTH_BTN_XPATH).click()
    assert web_driver.current_url == PAGE_LOGIN


def test_cabinet_btn_auth_success(web_driver):
    web_driver.get(PAGE_MAIN)
    web_driver.find_element(By.XPATH, MAIN_CABINET_BTN_XPATH).click()
    assert web_driver.current_url == PAGE_LOGIN


def test_registration_page_auth_success(web_driver):
    web_driver.get(PAGE_REGISTER)
    web_driver.find_element(By.XPATH, REGISTER_LOGIN_LINK_XPATH).click()
    assert web_driver.current_url == PAGE_LOGIN


def test_remind_page_auth_success(web_driver):
    web_driver.get(PAGE_REMIND_PWD)
    web_driver.find_element(By.XPATH, REMIND_PWD_LOGIN_LINK_XPATH).click()
    assert web_driver.current_url == PAGE_LOGIN
