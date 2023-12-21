FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /requirements.txt

COPY . /app/

WORKDIR /app/
