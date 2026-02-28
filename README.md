# **Автотесты для сервиса Stellar Burgers (Sprint 5)**
 ### Финальный проект по автоматизации тестирования веб-интерфейса сервиса «Космический фастфуд» с использованием Selenium и pytest.

# Описание проекта
 ### Проект содержит набор автоматизированных тестов для проверки ключевой функциональности сайта Stellar Burgers:

1. Регистрация пользователей (валидная и с ошибками).
2. Вход в систему через различные точки входа.
3. Навигация (переходы в личный кабинет, конструктор, по логотипу).
4. Выход из аккаунта.
5. Работа разделов конструктора (Булки, Соусы, Начинки).


### Структура проекта

Sprint_5 \
* tests/ &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Тесты, распределенные по функциональности
    * test_constructor.py
    * test_login.py
    * test_logout
    * test_navigation.py
    * test_registration.py
* .gitignore &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Игнорируемые файлы (venv, .pytest_cache, и т.д.)
* conftest.py&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Фикстуры для запуска драйвера и подготовки данных
* generator.py &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Генераторы случайных логинов (email) и паролей
* locators.py &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Локаторы Стеллар Бургерс 
* README.md &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Описание проекта
* requirements.txt &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Список зависимостей

# Запуск тестов
### Установи зависимости:
```c
pip install -r requirements.txt
pytest tests -v
