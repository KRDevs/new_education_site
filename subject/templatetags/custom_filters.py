import os, random
from django import template

register = template.Library()


@register.filter
def basename(value):
    return os.path.basename(value)


@register.filter
def shuffle(queryset):
    queryset_list = list(queryset)
    random.shuffle(queryset_list)
    return queryset_list
