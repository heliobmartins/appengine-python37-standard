import flask

from api.api_definition import api_v1
from messages.content_messages import NewContentRequest
from services.content_service import ContentService
from settings.decorators.api_decorator import route


# noinspection PyMethodParameters
@api_v1(name="content_api", url_prefix="contents")
class ContentApi:
    @route(methods=['POST'])
    def new_content():
        service = ContentService.get_instance()
        return service.create_content(NewContentRequest(flask.request.json))
