# Установка проекта
```https://python-poetry.org/docs/ установка poetry```
```poetry install```

# Проверка, что работают тесты
```python manage.py test```

# Запуск проекта
```python manage.py runserver 0.0.0.0:4096```

# Создание робота с параметрами

(Используется клиент https://httpie.io/)

```http POST localhost:4096/robots/ model="R2" version="D2" created="2023-01-01 00:00:00" --form```

# Скачивание отчета по производству за неделю

```http://localhost:4096/robots/excel_reports/summary_for_week.xlsx```

# Создание заказа

```http POST localhost:4096/robots/order customer="test@example.com" robot_serial="R2 D2" --form```

# Добавление в лист ожидания по несуществующему роботу

```http POST localhost:4096/robots/order customer="test@example.com" robot_serial="R2 D5" --form```
