from django import template

register = template.Library()

@register.filter
def replace_sfr(text):
    return text.replace('{%sfr%}', '')


@register.filter()
def load_image(symbol):
    images = {'gs': 'gs.jpg', 'jobs': 'jobs.png', 'ngg': 'ngg.png'}
    return images[symbol.lower()]
