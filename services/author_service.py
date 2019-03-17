import flask
from schematics.exceptions import DataError

from domain.author_domain import AuthorDomain


class AuthorService:
    __instance = None

    def __init__(self):
        if AuthorService.__instance is not None:
            raise Exception("This class is a Singleton")
        else:
            AuthorService.__instance = self

    @classmethod
    def get_instance(cls):
        if AuthorService.__instance is None:
            AuthorService()
        return AuthorService.__instance

    def create_author(self, author_request):
        error = self._validate_request(author_request)
        # TODO 1: Refactor and find a better way to manage the errors.
        # TODO 2 : Does this Schematics makes sense to validate requests?
        if error is not None:
            return error

        self._validate_fields(author_request)
        return self._save(author_request)

    def get_author(self, id):
        try:
            # TODO 4: Is it a good idea to wrap the values like below? Or would it be better option below
            # flask.jsonify(AuthorDomain.get_author(id).to_dict())
            return flask.jsonify({'author': AuthorDomain.get_user(
                id).to_dict()})  # TODO 8: If doesn't exits, instead of null, it should return 404.
        except:
            flask.abort(404)

    def update_author(self, update_request):
        error = self._validate_request(update_request)
        if error is not None:
            return error
        return flask.jsonify({'author': AuthorDomain.update_author(update_request)})

    def delete_author(self, id):
        try:
            AuthorDomain.delete_author(id)
            return flask.jsonify({'success': True})
        except:
            flask.abort(404)

    def _validate_request(self, author_request):
        try:
            author_request.validate()
        except DataError as err:
            # TODO 3: Discover a better standar to return the errors.
            return flask.jsonify({'errors': err.to_primitive()}), 400

    def _validate_fields(self, author_request):
        if author_request.name < 2:
            yield 'Name is too short, shall we type a bit more? Here I can do customised validations...'

    def _save(self, author_request):
        return flask.jsonify({'author': AuthorDomain.add_author(author_request)}), 201
