
revise-dev:
	cp .env.dev .env && python env_to_ini.py && alembic revision --autogenerate -m ""
upgrade-dev:
	cp .env.dev .env && alembic upgrade head
downgrade-dev:
	alembic downgrade -1