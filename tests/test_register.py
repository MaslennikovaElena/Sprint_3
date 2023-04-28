from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import USER_NAME, USER_EMAIL, PASSWORD, WRONG_PASSWORD, REGISTER_WRONG_PWD_MESSAGE
from locators import RegisterLocator, LoginLocator, MainLocator, CabinetLocator
from urls import PAGE_REGISTER


def test_register_success(web_driver):
    web_driver.get(PAGE_REGISTER)

    web_driver.find_element(By.XPATH, RegisterLocator.NAME_INPUT_XPATH).send_keys(USER_NAME)
    web_driver.find_element(By.XPATH, RegisterLocator.EMAIL_INPUT_XPATH).send_keys(USER_EMAIL)
    web_driver.find_element(By.XPATH, RegisterLocator.PASSWORD_INPUT_XPATH).send_keys(PASSWORD)

    web_driver.find_element(By.XPATH, RegisterLocator.SUBMIT_BTN_XPATH).click()
    WebDriverWait(web_driver, 10).until_not(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterLocator.SUBMIT_BTN_XPATH))
    )
    # Пробуем авторизоваться после регистрации
    web_driver.find_element(By.XPATH, LoginLocator.NAME_INPUT_XPATH).send_keys(USER_EMAIL)
    web_driver.find_element(By.XPATH, LoginLocator.PASSWORD_INPUT_XPATH).send_keys(PASSWORD)
    web_driver.find_element(By.XPATH, LoginLocator.AUTHORIZE_BTN_XPATH).click()

    # ожидание когда выполнится авторизация
    WebDriverWait(web_driver, 20).until_not(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginLocator.REMIND_PWD_LINK_XPATH))
    )
    # После авторизации выбрасывает на главный экран и надо перейти в кабинет что бы убедиться что авторизация удалась
    web_driver.find_element(By.XPATH, MainLocator.CABINET_BTN_XPATH).click()
    WebDriverWait(web_driver, 20).until(
        expected_conditions.visibility_of_element_located((By.XPATH, CabinetLocator.PROFILE_LINK_XPATH))
    )
    # получаем Логин пользователя получившийся в результате регистрации
    profile_login = web_driver.find_element(By.XPATH, CabinetLocator.PROFILE_LOGIN_FIELD_XPATH).get_property("value")
    assert profile_login == USER_EMAIL


def test_register_wrong_pwd_error_msg(web_driver):
    web_driver.get(PAGE_REGISTER)
    web_driver.find_element(By.XPATH, RegisterLocator.PASSWORD_INPUT_XPATH).send_keys(WRONG_PASSWORD)
    web_driver.find_element(By.XPATH, RegisterLocator.SUBMIT_BTN_XPATH).click()
    element = web_driver.find_element(By.CSS_SELECTOR, RegisterLocator.WRONG_PWD_MESSAGE_CSS)
    assert element.text == REGISTER_WRONG_PWD_MESSAGE
