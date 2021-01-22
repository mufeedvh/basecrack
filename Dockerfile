FROM python:3

WORKDIR /app

COPY . /app

RUN apt-get update &&\
    apt-get -y install tesseract-ocr libtesseract-dev &&\
    python -m pip install -r requirements.txt

WORKDIR /data

ENTRYPOINT [ "python", "/app/basecrack.py" ]