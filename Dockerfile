FROM python:3.11-slim

WORKDIR /app
COPY app /app
RUN pip install flask gunicorn

EXPOSE 8443

CMD ["gunicorn", "--certfile=certs/cert.pem", "--keyfile=certs/key.pem", "-b", "0.0.0.0:8443", "main:app"]

