FROM python:3.8-alpine  

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY app.py app.py

COPY templates templates

CMD ["python", "app.py"]