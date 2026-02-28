from selenium.webdriver.common.by import By

class TestLocators:
       
    # РЕГИСТРАЦИЯ 
    REG_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") # Поле имя
    REG_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле e-mail 
    REG_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # Поле пароль
    REG_REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    REG_PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]") # Ошибка "Некорректный пароль"
    REG_LOGIN_LINK = (By.LINK_TEXT, "Войти") # Ссылка перехода на вход
    # ВХОД 
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле e-mail
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # Поле пароль
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка войти
    FORGOT_LOGIN_LINK = (By.LINK_TEXT, "Войти") # Ссылка "Войти" на странице восстановления пароля
    # ГЛАВНАЯ
    MAIN_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    MAIN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    MAIN_CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']") # Главный заголовок
    # ТАБЫ КОНСТРУКТОРА
    TAB_BUNS = (By.XPATH, ".//span[text()='Булки']") # Таб Булки
    TAB_SAUCES = (By.XPATH, ".//span[text()='Соусы']") # Таб Соусы
    TAB_FILLINGS = (By.XPATH, ".//span[text()='Начинки']") # Таб Начинки
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]") # Поиск активного таба
    # ЗАГОЛОВОК И ПРОФИЛЬ 
    HEADER_CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']") # Ссылка на Конструктор
    HEADER_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]") # Логотип Стеллар Бургерс
    HEADER_PROFILE_LINK = (By.LINK_TEXT, "Личный Кабинет") # Ссылка на Личный Кабинет
    PROFILE_EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка выхода из профиля
