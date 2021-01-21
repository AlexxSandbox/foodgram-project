from django import template

register = template.Library()


@register.simple_tag
def set_tags(request, value):
    request_object = request.GET.copy()
    tags = request_object.getlist('tag')
    if value in tags:
        tags.remove(value)
        request_object.setlist('tag', tags)
    else:
        tags.append(value)
        request_object.setlist('tag', tags)
    return request_object.urlencode()


@register.simple_tag
def set_page(request, value):
    request_object = request.GET.copy()
    request_object['page'] = value
    return request_object.urlencode()
