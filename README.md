# REST API для проекта Yatube

API для социальной сети Yatube, позволяющий работать с публикациями, комментариями, группами и подписками.

## Автор

**FispBG**

GitHub: https://github.com/FispBG

---

## Описание проекта

Проект предоставляет REST API для социальной платформы Yatube.

API позволяет:

- создавать, редактировать и удалять публикации;
- оставлять комментарии к постам;
- просматривать тематические сообщества;
- подписываться на авторов;
- выполнять поиск по подпискам;
- работать с JWT-аутентификацией.

---

## Технологии

- Python 3.8+
- Django 3.2
- Django REST Framework
- Djoser
- Simple JWT

---

## Возможности API

### Публикации (Posts)

- Получение списка публикаций
- Просмотр отдельной публикации
- Создание публикации
- Редактирование публикации
- Удаление публикации

### Комментарии (Comments)

- Получение комментариев к посту
- Создание комментариев
- Редактирование комментариев
- Удаление комментариев

### Сообщества (Groups)

- Просмотр списка сообществ
- Просмотр отдельного сообщества

> Доступ только для чтения.

### Подписки (Follow)

- Подписка на авторов
- Просмотр своих подписок
- Поиск подписок по username

---

## Установка проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/FispBG/api_final_yatube_ad.git
cd api_final_yatube_ad
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

#### Windows (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Применение миграций

```bash
python yatube_api/manage.py migrate
```

### 5. Запуск сервера

```bash
python yatube_api/manage.py runserver
```

---

## Документация API

После запуска проекта документация Redoc будет доступна по адресу:

```text
http://127.0.0.1:8000/redoc/
```

---

## Аутентификация

В проекте используется JWT-аутентификация.

### Получение JWT-токена

```http
POST /api/v1/jwt/create/
Content-Type: application/json
```

Пример запроса:

```json
{
  "username": "user",
  "password": "password"
}
```

---

## Примеры запросов

### Получение списка публикаций

```http
GET /api/v1/posts/
```

### Получение публикаций с пагинацией

```http
GET /api/v1/posts/?limit=10&offset=0
```

### Создание публикации

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "text": "Новый пост",
  "group": 1
}
```

---

## Работа с комментариями

### Получение комментариев поста

```http
GET /api/v1/posts/{post_id}/comments/
```

### Создание комментария

```http
POST /api/v1/posts/{post_id}/comments/
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "text": "Комментарий"
}
```

---

## Работа с подписками

### Просмотр подписок

```http
GET /api/v1/follow/
Authorization: Bearer <access_token>
```

### Поиск по подпискам

```http
GET /api/v1/follow/?search=username
Authorization: Bearer <access_token>
```

### Подписка на автора

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json
```

```json
{
  "following": "author_username"
}
```

---

## Права доступа

### Анонимные пользователи

- Доступ только на чтение
- Раздел подписок недоступен

### Авторизованные пользователи

- Могут создавать контент
- Могут редактировать и удалять только свои записи

---

## Структура API

| Endpoint | Методы | Описание |
|---|---|---|
| `/api/v1/posts/` | GET, POST | Работа с публикациями |
| `/api/v1/posts/{id}/` | GET, PUT, PATCH, DELETE | Работа с конкретной публикацией |
| `/api/v1/posts/{post_id}/comments/` | GET, POST | Комментарии поста |
| `/api/v1/groups/` | GET | Список групп |
| `/api/v1/follow/` | GET, POST | Подписки |

---

## Пример ответа API

```json
{
  "id": 1,
  "author": "FispBG",
  "text": "Привет, Yatube!",
  "pub_date": "2026-05-26T12:00:00Z"
}
```

---

## Лицензия

Проект создан в учебных целях.
