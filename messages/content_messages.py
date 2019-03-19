from schematics import Model
from schematics.types import StringType


class NewContentRequest(Model):
    title = StringType(required=True)
    description = StringType(required=True, max_length=150)
    body = StringType(required=True)

