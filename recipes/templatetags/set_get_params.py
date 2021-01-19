from django import template

register = template.Library()


@register.simple_tag
def set_tags(request, tags, value):
    request_object = request.GET.copy()
    if request.GET.get(value):
        request_object.pop(value)
    elif value in tags:
        for tag in tags:
            if tag != value:
                request_object[tag] = value
    else:
        request_object[value] = value

    return request_object.urlencode()


@register.simple_tag
def set_page(request, value):
    request_object = request.GET.copy()
    request_object["page"] = value
    return request_object.urlencode()
