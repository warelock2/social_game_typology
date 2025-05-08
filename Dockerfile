FROM python:3.11-slim

WORKDIR /app
COPY app /app
RUN pip install flask gunicorn

EXPOSE 3443

CMD ["gunicorn", "--certfile=certs/cert.pem", "--keyfile=certs/key.pem", "-b", "0.0.0.0:3443", "main:app"]

