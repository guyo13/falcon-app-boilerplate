import asyncio
import logging
import falcon

from app.utils.timers import set_timeout, set_interval


class DemoController:

    def __init__(self, config):
        self._config = config
        self._ready = False

    async def init_async(self):
        """ This function allows calling async functions
            as part of the initialization of the app
        """
        print("Async code called on startup")
        if self._ready is not True:
            self._ready = True

    async def on_get(self, req, resp):
        # Return a json response
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {"Hello": "World"}
    
    async def on_post(self, req, resp):
        resp.content_type = falcon.MEDIA_JSON
        try:
            # Try to automatically parse the request body according to the Content-Type header.
            # See https://falcon.readthedocs.io/en/stable/api/media.html#content-type-negotiation
            # and https://falcon.readthedocs.io/en/stable/api/request_and_response_asgi.html#falcon.asgi.Request.get_media
            media = await req.get_media()
        except Exception:
            logging.exception('Bad request')
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'Malformed request'}
        else:
            resp.status = falcon.HTTP_200
            resp.media = {'status': 'OK'}

    async def on_get_test1(self, req, resp):
        resp.media = {"status": "test1 api called"}
