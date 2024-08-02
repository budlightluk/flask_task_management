# Flask Task Management

Это простое веб-приложение для управления задачами, созданное с использованием Flask. Оно позволяет пользователям регистрироваться, входить в систему, создавать, редактировать и удалять задачи.

## Установка

1. Клонируйте репозиторий на ваш локальный компьютер:
    ```bash
    git clone https://github.com/yourusername/flask_task_management.git
    ```

2. Перейдите в каталог проекта:
    ```bash
    cd flask_task_management
    ```

3. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Для Windows
    # source venv/bin/activate  # Для MacOS/Linux
    ```

4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

5. Инициализируйте базу данных:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

## Запуск

1. Запустите приложение:
    ```bash
    flask run
    ```

2. Перейдите в браузере по адресу `http://127.0.0.1:5000/`.

## Структура проекта

- `app/`
  - `__init__.py` — инициализация приложения Flask и расширений.
  - `models.py` — модели базы данных для пользователей и задач.
  - `forms.py` — формы для входа, регистрации и создания задач.
  - `routes.py` — маршруты для обработки HTTP-запросов.
  - `templates/` — HTML-шаблоны для отображения страниц.
- `migrations/` — директория для хранения миграций базы данных.
- `venv/` — виртуальное окружение.
- `config.py` — конфигурация приложения.
- `requirements.txt` — список зависимостей.

## Основные функции

- Регистрация пользователей
- Авторизация пользователей
- Создание, редактирование и удаление задач
- Отображение списка задач

## Зависимости

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- Werkzeug

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробнее см. файл [LICENSE](LICENSE).

Danila Ladygin
budlighterluk@gmail.com
@SkyWalker_OG
