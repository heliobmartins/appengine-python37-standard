import flask
from schematics.exceptions import DataError

from domain.content_domain import ContentDomain


class ContentService:
    __instance = None

    def __init__(self):
        if ContentService.__instance is not None:
            raise Exception("This class is a Singleton")
        else:
            ContentService.__instance = self

    @classmethod
    def get_instance(cls):
        if ContentService.__instance is None:
            ContentService()
        return ContentService.__instance

    def create_content(self, content_request):
        error = self.validate_request(content_request)
        if error is not None:
            return error
        self.validate_fields(content_request)
        return flask.jsonify({'content': ContentDomain.add_content(content_request)}), 201

    def validate_request(self, content_request):
        try:
            content_request.validate()
        except DataError as err:
            return flask.jsonify({'errors': err.to_primitive()}), 400

    def validate_fields(self, content_request):
        pass  # Here we can have custom validations for each value in the request.
