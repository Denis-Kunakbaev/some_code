# d.kunakbaev
# Тестовый проект для сайта demoqa.com

Этот проект содержит набор автоматических тестов для сайта [demoqa.com](https://demoqa.com/).

## Функциональность

Проект включает в себя следующие тесты:

- Тестирование формы Web Tables:
    - Добавление нового пользователя в таблицу.
    - Проверка наличия пользователя в таблице.
    - Удаление нового пользователя из таблицы.
- Тестирование формы Browser Windows:
    - Открытие новой вкладки.
    - Переход на новую вкладку.
    - Закрытие текущей вкладки.
    - Переход на страницу "Links".

## Требования

- Python 3.x
- Selenium
- PyTest
- webdriver-manager

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Denis-Kunakbaev/some_code.git

Установите зависимости:
pip install -r requirements.txt


Запуск тестов
Запустите тесты с помощью pytest:
pytest


Структура проекта
├── Pages
│   ├── main_page.py
│   └── web_tables_form.py
├── Forms
│   ├── base_form.py
│   └── web_tables_form.py
├── Elements
│   ├── tabs.py
│   └── button.py
└── tests
    └── test_tables.py

Дополнительные сведения
requirements.txt содержит список необходимых зависимостей.
tests папка содержит тестовые файлы.
Pages папка содержит файлы с описанием страниц.
Elements папка содержит файлы с описанием веб-элементов.
Forms папка содержит файлы с описанием форм.
Автор
Denis-Kunakbaev