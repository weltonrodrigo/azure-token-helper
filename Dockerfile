FROM python:3.10-slim

RUN pip install --no-cache-dir --upgrade poetry

WORKDIR /code

COPY ./poetry.lock ./pyproject.toml /code/

RUN poetry export > /code/requirements.txt

# RUN poetry install

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app.py /code/app.py
COPY ./config.py /code/config.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
