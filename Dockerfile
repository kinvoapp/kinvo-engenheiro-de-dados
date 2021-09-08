FROM python:3.9.6-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir wheel 'poetry==1.1.8' && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi && \
    chmod +x entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]