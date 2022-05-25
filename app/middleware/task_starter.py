import asyncio


class TaskStarterMW:
    def __init__(self, on_startup, *args, **kwargs):
        """
        :param on_startup - A callable to run on process_startup
        """
        self.on_startup = (on_startup, args, kwargs)

    async def process_startup(self, scope, event):
        """ Calls an async function before the server starts accepting requests"""
        _len = len(self.on_startup)
        if self.on_startup is not None and _len > 0:
            args = self.on_startup[1] if _len > 1 else tuple()
            kwargs = self.on_startup[2] if _len > 2 else dict()
            call = self.on_startup[0](*args, **kwargs)
        if asyncio.iscoroutine(call):
            await call
        """Process the ASGI lifespan startup event.

        Invoked when the server is ready to start up and
        receive connections, but before it has started to
        do so.

        To halt startup processing and signal to the server that it
        should terminate, simply raise an exception and the
        framework will convert it to a "lifespan.startup.failed"
        event for the server.

        Args:
            scope (dict): The ASGI scope dictionary for the
                lifespan protocol. The lifespan scope exists
                for the duration of the event loop.
            event (dict): The ASGI event dictionary for the
                startup event.
        """

    async def process_shutdown(self, scope, event):
        """Process the ASGI lifespan shutdown event.

        Invoked when the server has stopped accepting
        connections and closed all active connections.

        To halt shutdown processing and signal to the server
        that it should immediately terminate, simply raise an
        exception and the framework will convert it to a
        "lifespan.shutdown.failed" event for the server.

        Args:
            scope (dict): The ASGI scope dictionary for the
                lifespan protocol. The lifespan scope exists
                for the duration of the event loop.
            event (dict): The ASGI event dictionary for the
                shutdown event.
        """

    async def process_request(self, req, resp):
        """Process the request before routing it.

        Note:
            Because Falcon routes each request based on req.path, a
            request can be effectively re-routed by setting that
            attribute to a new value from within process_request().

        Args:
            req: Request object that will eventually be
                routed to an on_* responder method.
            resp: Response object that will be routed to
                the on_* responder.
        """

    async def process_resource(self, req, resp, resource, params):
        """Process the request after routing.

        Note:
            This method is only called when the request matches
            a route to a resource.

        Args:
            req: Request object that will be passed to the
                routed responder.
            resp: Response object that will be passed to the
                responder.
            resource: Resource object to which the request was
                routed.
            params: A dict-like object representing any additional
                params derived from the route's URI template fields,
                that will be passed to the resource's responder
                method as keyword arguments.
        """

    async def process_response(self, req, resp, resource, req_succeeded):
        """Post-processing of the response (after routing).

        Args:
            req: Request object.
            resp: Response object.
            resource: Resource object to which the request was
                routed. May be None if no route was found
                for the request.
            req_succeeded: True if no exceptions were raised while
                the framework processed and routed the request;
                otherwise False.
        """

    async def process_request_ws(self, req, ws):
        """Process a WebSocket handshake request before routing it.

        Note:
            Because Falcon routes each request based on req.path, a
            request can be effectively re-routed by setting that
            attribute to a new value from within process_request().

        Args:
            req: Request object that will eventually be
                passed into an on_websocket() responder method.
            ws: The WebSocket object that will be passed into
                on_websocket() after routing.
        """

    async def process_resource_ws(self, req, ws, resource, params):
        """Process a WebSocket handshake request after routing.

        Note:
            This method is only called when the request matches
            a route to a resource.

        Args:
            req: Request object that will be passed to the
                routed responder.
            ws: WebSocket object that will be passed to the
                routed responder.
            resource: Resource object to which the request was
                routed.
            params: A dict-like object representing any additional
                params derived from the route's URI template fields,
                that will be passed to the resource's responder
                method as keyword arguments.
        """
