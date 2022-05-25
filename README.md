# Falcon + Uvicorn ASGI app

This is an example of a web server that utilizes asyncio processing using the [Falcon](https://falcon.readthedocs.io/en/stable/index.html) web framework and running on [uvicorn](https://www.uvicorn.org/) ASGI web server.

## Setup
Create a virtualenv: `python -m venv venv`

Activate it: `. venv/bin/activate`

Install base requirements: `pip install -r requirements.txt`

Run the `run.sh` script to start the app.

## Configuring

Both App and Uvicorn configuration should reside in an optional `conf.d` directory that resides in the CWD of the app and is not committed to source control.

To configure uvicorn copy the example in `examples/uvicorn` to your `conf.d/` directory and modify it accordingly.

To configure the app copy the example in `examples/config.json.example` to `conf.d/config.json` modify it accordingly.

## Structure

```sh
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── app.py
│   ├── asgi.py
│   ├── config.py
│   ├── constants.py
│   ├── middleware
│   │   ├── __init__.py
│   │   └── task_starter.py
│   ├── resources
│   │   ├── __init__.py
│   │   ├── demo
│   │   │   ├── __init__.py
│   │   │   └── demo_controller.py
│   │   └── status
│   │       ├── __init__.py
│   │       └── ping.py
│   └── utils
│       ├── async_utils.py
│       └── timers.py
├── docker-entrypoint.sh
├── examples
│   ├── config.json.example
│   └── uvicorn
├── requirements.txt
└── run.sh
```

The `app/app.py` module contains the main initialization code - including config loading and CORS setup - which also starts the falcon framework.

The `app/asgi.py` module creates the falcon app and is executed by the ASGI server.

The `app/config.py` module defines a `Config` class that you should extend with your own config parameters.

The `app/constants.py` module is the place to define app constants.

The `app/utils` module contains submodules that define some useful functions for working with async Python code.

The `app/middleware` module is where middleware classes should be placed, it contains a default `task_starter.py` module to help with async initialization of controllers.

The `app/resources` module is where endpoint controllers should be placed, it contains a simple healthcheck endpoint and an example of a controller with suffix endpoints.

The `examples` folder contains example configuration files for the app and for uvicorn.

The `examples/uvicorn` is a simple script that can be sourced to configure uvicorn at run time.

The `examples/config.json.example` is a template for the JSON configuration file the app tries to read on startup.

## License

This boilerplate uses the UNLICENSE model. See the `LICENSE.UNLICENSE` file.