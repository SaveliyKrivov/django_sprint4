# Blogicum

**Blogicum** — это веб-приложение для ведения блогов, разработанное на Django. Пользователи могут создавать и публиковать записи, просматривать посты других авторов, а также оставлять комментарии. Проект реализует основные функции блог-платформы и демонстрирует навыки работы с Django, HTML и другими технологиями.

![main_page](https://github.com/user-attachments/assets/621ccbe7-487e-4292-8581-73a30c99f567)
![category_page](https://github.com/user-attachments/assets/c54de289-6e41-476b-b4af-4755124928fe)
![profile_page](https://github.com/user-attachments/assets/e34fa113-74b3-497c-8fb1-174910c52405)

## 🚀 Функциональность

- Регистрация и аутентификация пользователей
- Создание, редактирование и удаление постов
- Добавление изображений к публикациям
- Комментирование записей других пользователей
- Категоризация постов по тематикам и локациям
- Пагинация списка публикаций
- Административная панель для управления контентом

## 🛠 Технологии

- Python 3.9
- Django 3.2
- SQLite
- HTML, CSS (Bootstrap)
- Pillow
- pytest
- pre-commit (линтинг и форматирование)

## 📦 Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/SaveliyKrivov/blogicum.git
   cd blogicum
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   .\venv\Scripts\activate   # Для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции и загрузите фикстуры:

   ```bash
   python manage.py migrate
   python manage.py loaddata db.json
   ```

5. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

После запуска приложение будет доступно по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## ✅ Тестирование

Для запуска тестов выполните:

```bash
pytest
```

## 🔗 Полезные ссылки

- [Репозиторий на GitHub](https://github.com/SaveliyKrivov/blogicum.git)

---
