def convert_entity_into_to(content):
    dest = {
        u'title': content.title,
        u'description': content.description,
        u'body': content.body
    }
    return dest


def convert_to_into_entity(content_to):
    from domain.content_domain import ContentDomain
    return ContentDomain(title=content_to.title,
                         description=content_to.description,
                         body=content_to.body)
