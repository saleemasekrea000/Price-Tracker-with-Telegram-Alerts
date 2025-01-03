FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY src /app/src/
#COPY alembic /app/alembic/
#COPY alembic.ini /app/alembic.ini


