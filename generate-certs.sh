#!/bin/bash
mkdir -p certs
openssl req -x509 -newkey rsa:4096 -sha256 -days 365 \
  -nodes -keyout certs/key.pem -out certs/cert.pem \
  -subj "/C=US/ST=State/L=City/O=Company/OU=Org/CN=localhost"

