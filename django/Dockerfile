FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install --upgrade pip

COPY ./src/requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY ./src /src

RUN chmod +x entry_point.sh