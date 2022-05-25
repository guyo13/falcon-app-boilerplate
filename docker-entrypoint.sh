#!/bin/bash
set -e

if [ "$1" = 'run-app' ]; then
    args=""
    if [ -f conf.d/uvicorn ]
    then
      source conf.d/uvicorn
      # UVICORN_HOST="0.0.0.0"
      # UVICORN_PORT="5000"
      # UVICORN_SSL_KEY_FILE=""
      # UVICORN_SSL_CERT_FILE=""
      # UVICORN_SSL_CA_CERTS_FILE=""
      # UVICORN_SSL_KEY_FILE_PASS=""
      # UVICORN_SSL_VER="5"
      # UVICORN_SSL_CIPHERS=""
      if [ "$UVICORN_HOST" != "" ]
      then
        args="$args --host $UVICORN_HOST"
      fi
      if [ "$UVICORN_PORT" != "" ]
      then
        args="$args --port $UVICORN_PORT"
      fi
      if [ "$UVICORN_SSL_KEY_FILE" != "" ]
      then
        args="$args --ssl-keyfile $UVICORN_SSL_KEY_FILE"
      fi
      if [ "$UVICORN_SSL_CERT_FILE" != "" ]
      then
        args="$args --ssl-certfile $UVICORN_SSL_CERT_FILE"
      fi
      if [ "$UVICORN_SSL_CA_CERTS_FILE" != "" ]
      then
        args="$args --ssl-ca-certs $UVICORN_SSL_CA_CERTS_FILE"
      fi
      if [ "$UVICORN_SSL_KEY_FILE_PASS" != "" ]
      then
        args="$args --ssl-keyfile-password $UVICORN_SSL_KEY_FILE_PASS"
      fi
      if [ "$UVICORN_SSL_VER" != "" ]
      then
        args="$args --ssl-version $UVICORN_SSL_VER"
      fi
      if [ "$UVICORN_SSL_CIPHERS" != "" ]
      then
        args="$args --ssl-ciphers $UVICORN_SSL_CIPHERS"
      fi
    fi
    exec uvicorn $args app.asgi:app
fi

exec "$@"
