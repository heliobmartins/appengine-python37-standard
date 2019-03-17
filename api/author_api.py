import flask
from flask import Blueprint

from messages.author_messages import NewAuthorRequest, UpdateAuthorRequest
from services.author_service import AuthorService

author_api = Blueprint('user_api', __name__)


# TODO 7 - Lot of service = AuthorService.get_instance(). Should I create a class and use it only once? (^.-)

@author_api.route('/authors', methods=['POST'])
def new_author():
    service = AuthorService.get_instance()
    return service.create_author(NewAuthorRequest(flask.request.json))


@author_api.route('/authors/<id>')
def read_user(id):
    service = AuthorService.get_instance()  # TODO 9 - How to assure that ID has been filled?
    return service.get_author(id)


@author_api.route('/authors/<id>', methods=['PUT'])
def update_user(id):
    service = AuthorService.get_instance()
    request = UpdateAuthorRequest(flask.request.json)
    request.id = id
    return service.update_author(UpdateAuthorRequest(request))


@author_api.route('/authors/<id>', methods=['DELETE'])
def delete_user(id):
    service = AuthorService.get_instance()
    return service.delete_author(id)
