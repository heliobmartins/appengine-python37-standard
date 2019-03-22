from settings.decorators.api_decorator import ApiRegistrar

api_v1 = ApiRegistrar(version='v1')


# noinspection PyUnresolvedReferences
def import_apis():
    import api.v1.author_api
    import api.v1.content_api


def initialise_apis(app):
    import_apis()
    register_apis(app)


def register_apis(app):
    for blueprint in list(api_v1.get_registered_apis().values()):
        app.register_blueprint(blueprint)
