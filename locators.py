


# Страница регистрации
# - Элемент ввода пароля
REGISTER_PASSWORD_INPUT_XPATH = ".//input[@type='password']"
# - Элемент ввода имени пользователя
REGISTER_NAME_INPUT_XPATH = ".//label[text()='Имя']/parent::div/input"
# - Элемент ввода почты пользователя
REGISTER_EMAIL_INPUT_XPATH = ".//label[text()='Email']/parent::div/input"
# - Кнопка выполнения регистрации
REGISTER_SUBMIT_BTN_XPATH = ".//button[text()='Зарегистрироваться']"
# - Элемент отображения ошибки ввода не верного пароля
REGISTER_WRONG_PWD_MESSAGE_CSS = "p.input__error"
# - Ссылка на переход к авторизации
REGISTER_LOGIN_LINK_XPATH = ".//a[text()='Войти']"

# Заглавная страница
# - Кнопка перехода к авторизации
MAIN_AUTH_BTN_XPATH = ".//button[text()='Войти в аккаунт']"
# - Кнопка перехода в личный кабинет
MAIN_CABINET_BTN_XPATH = ".//a/p[text()='Личный Кабинет']"

# Страница напоминания пароля
# - Ссылка для перехода на страницу авторизации
REMIND_PWD_LOGIN_LINK_XPATH = ".//a[text()='Войти']"

# Страница авторизации
# - Поле ввода имени пользователя
LOGIN_NAME_INPUT_XPATH = ".//label[text()='Email']//parent::*/input"
# - Поле ввода пароля
LOGIN_PASSWORD_INPUT_XPATH = ".//input[@type='password']"
# - Кнопка авторизации
LOGIN_AUTHORIZE_BTN_XPATH = ".//button[text()='Войти']"
# - Ссылка на востановление пароля
LOGIN_REMIND_PWD_LINK_XPATH = ".//a[text()='Восстановить пароль']"

# Личный кабинет
# - Кнопка перехода в конструктор
CABINET_CONSTRUCTOR_BTN_XPATH = ".//p[text()='Конструктор']/parent::a"
# - Кнопка выхода из аккаунта
CABINET_LOGOUT_BTN_XPATH = ".//button[text()='Выход']"
# - Лого сайта
CABINET_SITE_LOGO_XPATH = ".//div[contains(@class, 'logo')]/a"

# Конструктор
# - Ссылка Булки
CONSTRUCTOR_BREAD_LINK_XPATH = ".//span[text()='Булки']"
# - Ссылка Соусы
CONSTRUCTOR_SAUSE_LINK_XPATH = ".//span[text()='Соусы']"
# - Ссылка Начинки
CONSTRUCTOR_FILLING_LINK_XPATH = ".//span[text()='Начинки']"
# - Заголовок Булки
CONSTRUCTOR_BREAD_HEADER_XPATH = ".//h2[text()='Булки']"
# - Заголовок Соусы
CONSTRUCTOR_SAUSE_HEADER_XPATH = ".//h2[text()='Соусы']"
# - Заголовок Начинки
CONSTRUCTOR_FILLING_HEADER_XPATH = ".//h2[text()='Начинки']"
