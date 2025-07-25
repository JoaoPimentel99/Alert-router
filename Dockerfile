FROM python:3.10.16-alpine3.21

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY alert-router.py .

CMD ["fastapi", "dev", "alert-router.py", "--host", "0.0.0.0"]
