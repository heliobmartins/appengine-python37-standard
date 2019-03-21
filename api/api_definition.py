from settings.decorators.api_decorator import ApiRegistrar


# noinspection PyUnresolvedReferences
def import_apis():
    import api.author_api
    import api.content_api


def initialise_apis(app):
    import_apis()
    register_apis(app)


def register_apis(app):
    for blueprint in list(ApiRegistrar.get_instance().get_registered_apis().values()):
        app.register_blueprint(blueprint)
