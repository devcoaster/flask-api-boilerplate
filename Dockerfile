FROM python:3.9-buster

RUN apt update

WORKDIR /usr/src

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./server.py ./server.py
COPY ./app ./app
