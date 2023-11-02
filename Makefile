define setup_env
	$(eval ENV_FILE := $(1))
	@echo " - setup env $(ENV_FILE)"
	$(eval include $(1))
	$(eval export)
endef

define setup_db_env
	$(eval export PGPASSWORD=postgres)
endef

# environments
env_db:
	$(call setup_db_env)

env_local: env_db
	$(call setup_env, .env.local)


create_database: env_local
	docker-compose up db -d
	alembic upgrade head

alembic: env_local
	alembic ${command}

create_migration: env_local
	[ "${message}" ] || ( echo "'messsage' not provided"; exit 1 )
	docker-compose up db -d
	alembic revision --autogenerate -m "${message}"

upgrade_db: env_local
	docker-compose up db -d
	alembic upgrade head

python_shell: env_local
	poetry run python

run_local: env_local
	poetry run uvicorn src.server:server --host 0.0.0.0 --port 8000 --no-access-log  --reload

run_server: env_local
	docker-compose up


