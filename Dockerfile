FROM python:3.12-slim

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

RUN chmod +x price_server.sh
