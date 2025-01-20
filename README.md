## Applications FastAPI
### В сервисе реализовано:
- Принятие заявки.
- Обработка и запись в БД.
- Публикация информации о новой заявке в Kafka.
- Получение списка заявок с фильтрацией по имени пользователей и пагинацией.

### Эндпоинты:

- POST /api/v1/applications: Создание заявки.
- GET /api/v1/applications: Получение списка заявок.

#### Пример запроса на создание заявки:
```json
{
    "user_name": "user_name",
    "description": "description"
}
```


#### Пример ответа:
```json
{
    "user_name": "user_name",
    "description": "description",
    "id": 1,
    "created_at": "2025-01-19T11:45:39.923Z"
}
```




#### Запрос на получение списка заявок:
В запросе указывается user_name при необходимости, а так же параметры пагинации


#### Пример ответа:

```json
[
    {
        "user_name": "user_name",
        "description": "description",
        "id": 1,
        "created_at": "2025-01-19T11:45:39.923Z"
    }
]
```


## Технологии
Python, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Kafka, Docker

## Запуск проекта
- Склонируйте репозиторий
- Выполните команду: docker-compose up --build
- После запуска контейнеров, документация будет доступна по ссылке: http://localhost:8000/docs