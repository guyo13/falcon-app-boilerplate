#!/bin/bash

if [ -f "./conf.d/uvicorn" ]
then
    echo "Using uvicorn env configuration"
    source ./conf.d/uvicorn
fi

uvicorn app.asgi:app
