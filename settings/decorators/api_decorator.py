from flask import Blueprint


class ApiRegistrar:
    __instance = None
    _blueprint_instances = {}
    _blueprint = None

    def __init__(self):
        if ApiRegistrar.__instance is not None:
            raise Exception("This class is a Singleton")
        else:
            ApiRegistrar.__instance = self

    def __call__(self, cls):
        for name in dir(cls):
            attr = getattr(cls, name)
            if callable(attr) and hasattr(attr, 'route_kwargs'):
                path = str(attr.route_kwargs.pop('path', "/"))
                path = path if len(path) > 0 and path[0] is '/' else '/' + path
                endpoint = attr.route_kwargs.pop("endpoint", name)
                self._blueprint.add_url_rule(path, endpoint, attr, **attr.route_kwargs)

        return cls

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    def get_registered_apis(self):
        return self._blueprint_instances

    def register_blueprint(self, version, **kwargs):
        kwargs['url_prefix'] = self._build_url_prefix(version) + kwargs['url_prefix']
        self._blueprint = Blueprint(import_name=__name__, **kwargs)
        self._blueprint_instances[self._blueprint.name] = self._blueprint
        return self

    @staticmethod
    def _build_url_prefix(version):
        return f"/api/{version}/"


def route(**kwargs):
    def __wrapped(func):
        func.route_kwargs = kwargs
        return func

    return __wrapped


def api(version, **kwargs):
    return ApiRegistrar.get_instance().register_blueprint(version, **kwargs)
