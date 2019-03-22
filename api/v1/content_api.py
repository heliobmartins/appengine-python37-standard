import flask

from api.v1 import api_v1
from messages.content_messages import NewContentRequest
from services.content_service import ContentService
from settings.decorators.api_decorator import endpoint


# noinspection PyMethodParameters
@api_v1(name="content_api", url_prefix="contents")
class ContentApi:
    @endpoint(methods=['POST'])
    def new_content():
        service = ContentService.get_instance()
        return service.create_content(NewContentRequest(flask.request.json))
