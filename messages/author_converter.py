def convert_entity_into_to(author):
    dest = {
        u'id': author.id,
        u'name': author.name,
        u'email': author.email
    }
    if author.profile_picture is not None:
        dest[u'profile_picture'] = author.profile_picture
    return dest


def convert_to_into_entity(author_to):
    from domain.author_domain import AuthorDomain
    return AuthorDomain(name=author_to.name,
                        email=author_to.email,
                        profile_picture=author_to.profile_picture)
