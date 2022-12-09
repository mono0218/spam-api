FROM python:3.9-slim

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./app /app

WORKDIR app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000