from flask import current_app

from messages import content_converter


class ContentDomain:
    def __init__(self, title, description, body):
        self.title = title
        self.description = description
        self.body = body

    @staticmethod
    def from_dict(source):
        return content_converter.convert_to_into_entity(source)

    def to_dict(self):
        return content_converter.convert_entity_into_to(self)

    @classmethod
    def _get_collection(cls):
        return current_app.db.collection(u'contents')

    @classmethod
    def _get_new_document(cls):
        return cls._get_collection().document()

    @classmethod
    def add_content(cls, content_request):
        new_document = cls._get_new_document()
        content_entity = ContentDomain.from_dict(content_request)
        content_to = content_entity.to_dict()
        new_document.set(content_to)
        return content_to
