from django import template

register = template.Library()

@register.filter
def replace_sfr(text):
    return text.replace('{%sfr%}', '')