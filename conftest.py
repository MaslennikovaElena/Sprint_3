import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import PAGE_LOGIN, LOGIN_NAME_INPUT_XPATH, PASSWORD, LOGIN_PASSWORD_INPUT_XPATH, USER_EMAIL, \
    LOGIN_AUTHORIZE_BTN_XPATH, LOGIN_REMIND_PWD_LINK_XPATH


@pytest.fixture()
def web_driver():
    # Фикстура создания драйвера для работы в тестах
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--headless')  # добавили настройку

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    # Закрытие браузера в конце теста
    driver.quit()


@pytest.fixture()
def authorized(web_driver):
    web_driver.get(PAGE_LOGIN)
    web_driver.find_element(By.XPATH, LOGIN_NAME_INPUT_XPATH).send_keys(USER_EMAIL)
    web_driver.find_element(By.XPATH, LOGIN_PASSWORD_INPUT_XPATH).send_keys(PASSWORD)
    web_driver.find_element(By.XPATH, LOGIN_AUTHORIZE_BTN_XPATH).click()
    # ожидание когда выполнится авторизация
    WebDriverWait(web_driver, 10).until_not(
        expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_REMIND_PWD_LINK_XPATH))
    )

    return web_driver