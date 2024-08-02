FROM python:3.12.4

WORKDIR /hbt_tracker

COPY requirements.txt /hbt_tracker/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .