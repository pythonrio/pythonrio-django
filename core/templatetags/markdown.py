from markdownx.utils import markdownify
from django import template


register = template.Library()


@register.filter
def render_markdown(value):
    return markdownify(value)
