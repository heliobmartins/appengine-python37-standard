import flask

from messages.content_messages import NewContentRequest
from services.content_service import ContentService
from settings.decorators.api_decorator import api, route


# noinspection PyMethodParameters
@api(name="content_api", url_prefix="contents", version="v1")
class ContentApi:
    @route(methods=['POST'])
    def new_content():
        service = ContentService.get_instance()
        return service.create_content(NewContentRequest(flask.request.json))
