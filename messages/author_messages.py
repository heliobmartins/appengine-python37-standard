from schematics import Model
from schematics.types import StringType, URLType


class NewAuthorRequest(Model):
    name = StringType(required=True)
    email = StringType(required=True)
    profile_picture = URLType()


class UpdateAuthorRequest(Model):
    id = StringType(required=True)
    name = StringType()
    email = StringType()
    profile_picture = URLType()

# class AuthorResponse(dict):
# #     dest = {
# #         u'name': author.name,
# #         u'email': author.email
# #     }
# #     if author.profile_picture is not None:
# #         dest[u'profile_picture'] = author.profile_picture
# #     return dest
