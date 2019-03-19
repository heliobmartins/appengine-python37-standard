def initialise_apis(app):
    from api.author_api import author_api
    from api.content_api import content_api
    apis = [author_api, content_api]
    register_apis(app, apis)


def register_apis(app, apis):
    for api in apis:
        app.register_blueprint(api, url_prefix='/api/v1/')
