from flask import Blueprint


class ApiConstants:
    ROUTE_KWARGS = 'route_kwargs'
    RULE_FLASK_PARAM = 'rule'
    METHODS_FLASK_PARAM = 'methods'
    ENDPOINT_FLASK_PARAM = 'endpoint'


class ApiRegistrar:
    _blueprint_instances = {}
    _version = None

    def __init__(self, version):
        self._version = version

    def __call__(self, name, url_prefix, **kwargs):
        def create_routes(cls):
            built_url_prefix = self._build_url_prefix() + url_prefix
            blueprint = Blueprint(import_name=__name__, name=name, url_prefix=built_url_prefix, **kwargs)
            self._blueprint_instances[name] = blueprint
            for attr_name in dir(cls):
                attr = getattr(cls, attr_name)
                if callable(attr) and hasattr(attr, ApiConstants.ROUTE_KWARGS):
                    route_attributes = getattr(attr, ApiConstants.ROUTE_KWARGS)
                    rule = self.get_rule_after_validation(route_attributes.pop(ApiConstants.RULE_FLASK_PARAM))
                    endpoint_name = route_attributes.pop(ApiConstants.ENDPOINT_FLASK_PARAM, attr_name)
                    blueprint.add_url_rule(rule, endpoint_name, attr, **route_attributes)
            return cls

        return create_routes

    def get_registered_apis(self):
        return self._blueprint_instances

    def _build_url_prefix(self):
        return "/api/%s/" % self._version

    @staticmethod
    def get_rule_after_validation(rule):
        return "/" + rule if len(rule) > 0 and rule[0] != "/" else rule


def endpoint(methods, rule="", **kwargs):
    def route(func):
        kwargs[ApiConstants.RULE_FLASK_PARAM] = rule
        kwargs[ApiConstants.METHODS_FLASK_PARAM] = methods
        setattr(func, ApiConstants.ROUTE_KWARGS, kwargs)
        return func

    return route
