import flask
from flask import Blueprint

from messages.content_messages import NewContentRequest
from services.content_service import ContentService

content_api = Blueprint('content_api', __name__)


@content_api.route('/contents', methods=['POST'])
def new_author():
    service = ContentService.get_instance()
    return service.create_content(NewContentRequest(flask.request.json))
