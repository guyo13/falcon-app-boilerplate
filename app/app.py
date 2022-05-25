import json
import pathlib
import logging
import falcon.asgi
from .config import Config
from .resources.demo.demo_controller import DemoController
from .resources.status.ping import PingEndpoint
from .middleware.task_starter import TaskStarterMW


def create_app(config=None):
    # Load config from file
    if config is None:
        conf_file = pathlib.Path('conf.d/config.json')
        if conf_file.exists() and conf_file.is_file():
            with conf_file.open() as cf:
                try:
                    config_vars = json.loads(cf.read())
                except Exception as e:
                    # FIXME - configure logging
                    logging.exception('Error loading config file')
                    raise e
        else:
            config_vars = {}
        config = Config(config_vars)
    
    # Load app endpoints
    demo_controller = DemoController(config)
    ping_endpoint = PingEndpoint(config)
    # Optional: Add a middleware that hooks into the process startup lifecycle event
    # and runs async initialization code before the app accepts requests
    async_endpoint_starter = TaskStarterMW(demo_controller.init_async)

    # Add middleware
    middleware = []
    middleware.append(async_endpoint_starter)

    # Add CORS middleware
    if config.cors_enabled:
        cors_mw = falcon.CORSMiddleware(allow_origins=config.allowed_origins,
                                        expose_headers=config.exposed_headers)
        middleware.append(cors_mw)
        print(f'CORS enabled for {config.allowed_origins}')

    # Create the app
    app = falcon.asgi.App(middleware=middleware)

    # Add routes

    # Request handlers in the controller should be called "on_get", "on_post"
    # If we want more api endpoint in the controller we can use the `suffix` kwarg, for example:
    # POST and GET handlers will be named "on_post_test1", "on_get_test1"
    app.add_route('/api/v1/test1', demo_controller, suffix='test1')
    
    # POST and GET handlers will be named "on_post", "on_get" since there is no suffix
    app.add_route('/api/v1/default', demo_controller)

    # App healthcheck endpoint
    app.add_route('/api/v1/ping', ping_endpoint)

    return app
