import hashlib
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def profile_url(email):
    return f"https://s.gravatar.com/avatar/{hashlib.md5(email.encode('utf-8').strip().lower()).hexdigest()}?s=50&d=mp"