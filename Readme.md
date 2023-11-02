## RUN MIGRATIONS
- `pip install poetry`
- `poetry install`
- `poetry shell`
- `docker-compose up db -d`
- `alembic revision --autogenerate -m "Tables Added"`
- `alembic upgrade head`

## RUN APPLICATION

- docker-compose up
- Visit `http://127.0.0.1:8000/docs`

