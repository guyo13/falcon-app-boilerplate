import falcon


class PingEndpoint:
    def __init__(self, config):
        self._config = config

    async def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {'status': 'UP'}
        resp.status = falcon.HTTP_200
