# Planetary API

Planetary API is a RESTful API for managing astronomy shows, show themes, sessions, reservations, and tickets. The project is built on Django and Django REST Framework with JWT authentication support and auto-generated API documentation using Swagger.

## Features

- **AstronomyShow** – Manage astronomy shows.
- **ShowTheme** – Associate themes with shows.
- **PlanetariumDome** – Information about planetarium domes.
- **ShowSession** – Manage show sessions.
- **Reservation** – Manage reservations.
- **Ticket** – Issue tickets for sessions.

## Technologies

- Django & Django REST Framework
- JWT Authentication (using djangorestframework-simplejwt)
- API Documentation with Swagger (drf-yasg)
- Testing with pytest

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/planetary-api.git
   cd planetary-api
   ```
2. **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate         # Linux/MacOS
    # or
    venv\Scripts\activate            # Windows

    pip install -r requirements.txt
    ```

## Configuration
1. **Environment Setup:**
    Create a ```.env``` file in the root directory and set the necessary environment variables (e.g., DATABASE_URL, SECRET_KEY, etc.).
2. **Run Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
3. **Create a Superuser:**

    ```bash 
    python manage.py createsuperuser
    ```
   
## Running the Server
1. **Build the Docker image:**
    ```bash
    docker build -t planetary-api .
    ```
2. **Run the container:**
    ```bash
    docker run -d -p 8000:8000 --env-file .env planetary-api
    ```
Alternatively, if using Docker Compose:
```bash
docker-compose up --build
```
The API will be available at: http://localhost:8000/api/

## API Documentation
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Authentication
To access protected endpoints:

1. **Obtain a JWT by making a POST request to:**
    ```bash
    /api/token/
    ```
    with the following data:
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
   ```
2. **Use the obtained access token in the Authorization header:**
    ```makefile
    Authorization: Bearer <your_access_token>
    ```

## Testing
Run tests using pytest:
```bash
pytest
```