FROM python:3.10-slim

SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# git is required to install any dep with a commit sha
RUN apt-get update \
    && apt-get install -y --no-install-recommends git curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# disable pip cache
ENV PIP_NO_CACHE_DIR 1
ENV POETRY_VERSION 1.3.2
ENV POETRY_HOME /opt/poetry
ENV PATH "$PATH:$POETRY_HOME/bin"

# fixes alembic path issue
ENV PYTHONPATH /app
# writes logs without buffering
ENV PYTHONUNBUFFERED 1
# since we use a single process the bytecode cache is useless
ENV PYTHONDONTWRITEBYTECODE 1




COPY ./app/pyproject.toml  /app/

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false \
    && poetry install

COPY ./app /app

EXPOSE 8000

CMD ["sh", "/app/docker-entrypoint.sh"]
