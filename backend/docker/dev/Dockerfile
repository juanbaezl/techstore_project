FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y postgresql-server-dev-all gcc python3-dev libc6-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh