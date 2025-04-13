# DogSite API

DogSite — это API для управления записями о собаках и их породах.  
Проект реализован на Django + Django REST Framework с использованием PostgreSQL и Docker.

---

## 📦 Стек технологий

- Python 3.11
- Django 5.2
- Django REST Framework
- PostgreSQL 14
- Docker, Docker Compose

---

## 🚀 Установка и запуск проекта

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-username/dogsite.git
cd dogsite
```

### 2. Создать .env файл

```bash
cp .env.example .env
```

### 3. Собрать и запустить контейнеры

```bash
docker-compose up --build
```
- Сервис будет доступен по адресу:
```bash
http://localhost:8000/
```

---

## 🧩 Архитектура

Проект разделён на два основных ресурса:
- Breed (/api/breeds/)
  - Описание пород собак
  - Параметры: размер, дружелюбность, обучаемость, линька, потребность в физнагрузке

- Dog (/api/dogs/)
  - Описание собак
  - Параметры: имя, возраст, порода, пол, цвет, любимая еда и игрушка

Запросы к API обрабатываются через ViewSet'ы Django REST Framework.

---

##  Пример использования
-Добавление породы/собаки
!(images/create.jpg)
  
