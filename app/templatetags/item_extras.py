from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.simple_tag
def replace_underbar(string):
    replaced = string.replace('_', ' ')
    return replaced


@register.simple_tag
def get_scripts(profile_name):
    u = User.objects.get(username__exact=profile_name)
    p = u.profile.scripts.all()
    return p
