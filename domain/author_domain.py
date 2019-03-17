from flask import current_app

from messages import author_converter


class AuthorDomain:
    # TODO 10 - Find out how can I map properly the data types of Firestore.
    id = ''
    name = ''
    email = ''

    def __init__(self, name, email, profile_picture=None):
        self.name = name
        self.email = email
        self.profile_picture = profile_picture

    @staticmethod
    def from_dict(source):
        return author_converter.convert_to_into_entity(source)

    def to_dict(self):
        return author_converter.convert_entity_into_to(self)

    def __repr__(self):
        return (
            u'Author(name={}, email={}, id={}'.format(self.name, self.email, self.id))

    @classmethod
    def _get_collection(cls):
        return current_app.db.collection(u'authors')

    @classmethod
    def _get_new_document(cls):
        return cls._get_collection().document()

    @classmethod
    def _get_document_by_id(cls, id):
        return cls._get_collection().document(id)  # TODO 6 - There is something here with code smell because of the get()

    @classmethod
    def add_author(cls, author_request):
        new_document = cls._get_new_document()
        author_entity = AuthorDomain.from_dict(author_request)
        author_entity.id = new_document.id
        author_to = author_entity.to_dict()
        del author_to["id"]  # TODO 5 - Fix this biggg workaround. HAUHUA
        new_document.set(author_to)
        return author_to

    @classmethod
    def get_user(cls, id):
        return cls._get_document_by_id(id).get()

    @classmethod
    def update_author(cls, update_request):
        author_document = cls._get_document_by_id(update_request.id)
        author_entity = AuthorDomain.from_dict(update_request)
        author_to = author_entity.to_dict()
        del author_to["id"]  # TODO 5 - Fix this biggg workaround. HAUHUA
        author_document.set(author_to)  # If I do not get the reference, it returns the snapshot.
        return author_to

    @classmethod
    def delete_author(cls, id):
        cls._get_collection().document(id).delete()
