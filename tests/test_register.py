from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import USER_NAME, USER_EMAIL, PASSWORD, WRONG_PASSWORD, REGISTER_PASSWORD_INPUT_XPATH, \
    REGISTER_NAME_INPUT_XPATH, REGISTER_EMAIL_INPUT_XPATH, REGISTER_SUBMIT_BTN_XPATH, REGISTER_WRONG_PWD_MESSAGE_CSS, \
    PAGE_REGISTER, PAGE_LOGIN, REGISTER_WRONG_PWD_MESSAGE


def test_register_success(web_driver):
    web_driver.get(PAGE_REGISTER)

    web_driver.find_element(By.XPATH, REGISTER_NAME_INPUT_XPATH).send_keys(USER_NAME)
    web_driver.find_element(By.XPATH, REGISTER_EMAIL_INPUT_XPATH).send_keys(USER_EMAIL)
    web_driver.find_element(By.XPATH, REGISTER_PASSWORD_INPUT_XPATH).send_keys(PASSWORD)

    web_driver.find_element(By.XPATH, REGISTER_SUBMIT_BTN_XPATH).click()
    WebDriverWait(web_driver, 10).until_not(
        expected_conditions.visibility_of_element_located((By.XPATH, REGISTER_SUBMIT_BTN_XPATH))
    )
    assert web_driver.current_url == PAGE_LOGIN


def test_register_wrong_pwd_error_msg(web_driver):
    web_driver.get(PAGE_REGISTER)
    web_driver.find_element(By.XPATH, REGISTER_PASSWORD_INPUT_XPATH).send_keys(WRONG_PASSWORD)
    web_driver.find_element(By.XPATH, REGISTER_SUBMIT_BTN_XPATH).click()
    element = web_driver.find_element(By.CSS_SELECTOR, REGISTER_WRONG_PWD_MESSAGE_CSS)
    assert element.text == REGISTER_WRONG_PWD_MESSAGE
