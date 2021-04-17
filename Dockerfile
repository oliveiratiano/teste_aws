# Use Python Official Image as Base
FROM python:3

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt install gcc

RUN apt install make

RUN apt install unzip

ADD main.py /

CMD [ "python", "./main.py" ]
