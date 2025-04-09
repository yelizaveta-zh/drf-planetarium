#  🌌 Planetarium API
 
A RESTful API for managing a planetarium system, built with Django REST Framework.

The API allows users to manage astronomy shows, show themes, domes, sessions, reservations, and tickets.

---

## 🚀 Features

- Create, list, and manage astronomy shows
- Associate themes with shows
- Manage planetarium domes and sessions
- Make reservations and issue tickets (authenticated)
- JWT-based authentication for secure access

---

## 🛠 Technologies

- Python 3.11
- Django 5.1.6
- Django REST Framework 3.15.2
- PostgreSQL
- Docker & Docker Compose
- Simple JWT 5.5.0 for authentication

---

## ⚙️ Setup and Run with Docker

### 1. Clone the repository

```bash
git clone https://github.com/yelizaveta-zh/drf-planetarium.git
cd drf-planetarium
```

### 2. Create a `.env` file in the root directory with the following content:

``` python
DEBUG=1
SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
DATABASE_NAME=planetarium_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

### 3. Build and run the project using Docker:

``` bash
docker-compose up --build
```

### 4. Apply migrations and create a superuser:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

Once running, the API will be available at:

👉 http://localhost:8000
