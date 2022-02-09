# See: https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
FROM python:3.10-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.12

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY ./poetry.lock ./pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY ./app.py /code/app.py
COPY ./config.py /code/config.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
