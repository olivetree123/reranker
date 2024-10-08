FROM python:3.10-slim

WORKDIR /app

ADD models--BAAI--bge-reranker-v2-m3.tar /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY main.py /app

EXPOSE 5608

CMD ["python", "main.py"]