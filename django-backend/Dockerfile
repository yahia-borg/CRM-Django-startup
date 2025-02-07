FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./django_backend/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./django_backend app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
