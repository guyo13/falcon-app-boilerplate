import uuid

class Config:
    """ A class implementing the configuration for the Falcon app"""
    DEFAULT_UUID_GENERATOR = uuid.uuid4

    def __init__(self, config_vars, **kwargs):
        if config_vars is None:
            config_vars = dict()
        self.uuid_generator = kwargs.get('UUID_GENERATOR',
                                         Config.DEFAULT_UUID_GENERATOR)
        # CORS config
        cors = config_vars.get('cors', {})
        self.cors = {}
        cors_enabled = cors.get('enabled', False)
        cors_allowed_origins = cors.get('allowedOrigins', tuple())
        cors_origins = self.normalize_cors_origins_list(cors_allowed_origins)

        if cors_enabled is True and len(cors_origins) > 0:
            self.cors['enabled'] = True
            self.cors['allowedOrigins'] = cors_origins
            cors_expose_headers = cors.get('exposedHeaders', tuple())
            if len(cors_expose_headers) > 0:
                self.cors['exposedHeaders'] = tuple(cors_expose_headers)
        else:
            self.cors['enabled'] = False
            self.cors['allowedOrigins'] = tuple()

    @property
    def cors_enabled(self):
        return self.cors.get('enabled', False)

    @property
    def allowed_origins(self):
        return self.cors.get('allowedOrigins')

    @property
    def exposed_headers(self):
        return self.cors.get('exposedHeaders')

    @classmethod
    def normalize_cors_origins_list(cls, origins):
        """
            Normalizes list of origins, removing duplicates,
            disallowing null origin and returning a string -
            if '*' origin is specified.
            :param origins - Iterable of origins or a string
        """
        if isinstance(origins, str):
            return origins if origins.lower() != 'null' else ''
        origin_set = set(origins)
        if '*' in origin_set:
            return '*'
        else:
            return tuple(origin_set)
