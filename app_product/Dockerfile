FROM python:3.10

WORKDIR /app_product

COPY ./requirements.txt /app_product/
RUN pip install --no-cache-dir --upgrade -r /app_product/requirements.txt

COPY ./app /app_product/app
COPY .env /app_product

COPY ./migration /app_product/migration
COPY ./alembic.ini /app_product/alembic.ini

EXPOSE 80

CMD ["/bin/sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 80"]

