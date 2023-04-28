class RegisterLocator:
    """Локаторы для страницы регистрации"""

    PASSWORD_INPUT_XPATH = ".//input[@type='password']"
    """Элемент ввода пароля"""
    NAME_INPUT_XPATH = ".//label[text()='Имя']/parent::div/input"
    """Элемент ввода имени пользователя"""
    EMAIL_INPUT_XPATH = ".//label[text()='Email']/parent::div/input"
    """Элемент ввода почты пользователя"""
    SUBMIT_BTN_XPATH = ".//button[text()='Зарегистрироваться']"
    """Кнопка выполнения регистрации"""
    WRONG_PWD_MESSAGE_CSS = "p.input__error"
    """Элемент отображения ошибки ввода не верного пароля"""
    LOGIN_LINK_XPATH = ".//a[text()='Войти']"
    """Ссылка на переход к авторизации"""


class MainLocator:
    """Локаторы для заглавной страницы"""

    AUTH_BTN_XPATH = ".//button[text()='Войти в аккаунт']"
    """Кнопка перехода к авторизации"""
    CABINET_BTN_XPATH = ".//a/p[text()='Личный Кабинет']"
    """Кнопка перехода в личный кабинет"""


class RemindPwdLocator:
    """Локаторы для страницы напоминания пароля"""

    LOGIN_LINK_XPATH = ".//a[text()='Войти']"
    """Ссылка для перехода на страницу авторизации"""


class LoginLocator:
    """Локаторы для страницы авторизации"""

    NAME_INPUT_XPATH = ".//label[text()='Email']//parent::*/input"
    """Поле ввода имени пользователя"""
    PASSWORD_INPUT_XPATH = ".//input[@type='password']"
    """Поле ввода пароля"""
    AUTHORIZE_BTN_XPATH = ".//button[text()='Войти']"
    """Кнопка авторизации"""
    REMIND_PWD_LINK_XPATH = ".//a[text()='Восстановить пароль']"
    """Ссылка на востановление пароля"""


class CabinetLocator:
    """Локаторы для личного кабинета"""

    CONSTRUCTOR_BTN_XPATH = ".//p[text()='Конструктор']/parent::a"
    """Кнопка перехода в конструктор"""
    LOGOUT_BTN_XPATH = ".//button[text()='Выход']"
    """Кнопка выхода из аккаунта"""
    SITE_LOGO_XPATH = ".//div[contains(@class, 'logo')]/a"
    """Лого сайта"""


class ConstructorLocator:
    """Локаторы для конструктора"""

    BREAD_LINK_XPATH = ".//span[text()='Булки']"
    """Ссылка Булки"""
    SAUSE_LINK_XPATH = ".//span[text()='Соусы']"
    """Ссылка Соусы"""
    FILLING_LINK_XPATH = ".//span[text()='Начинки']"
    """Ссылка Начинки"""
    BREAD_HEADER_XPATH = ".//h2[text()='Булки']"
    """Заголовок Булки"""
    SAUSE_HEADER_XPATH = ".//h2[text()='Соусы']"
    """Заголовок Соусы"""
    FILLING_HEADER_XPATH = ".//h2[text()='Начинки']"
    """Заголовок Начинки"""
