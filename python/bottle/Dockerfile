FROM jfloff/alpine-python:3.6

RUN apk add --no-cache git

WORKDIR /app
COPY ./requirements.txt ./
RUN pip3 install -U pip && \
    pip3 install -U -r requirements.txt
COPY . ./
