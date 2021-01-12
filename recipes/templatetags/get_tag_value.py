from django import template

from recipes.models import TAGS_CHOICES

register = template.Library()


@register.filter
def get_tag_value(tag):
    return dict(TAGS_CHOICES)[tag]
