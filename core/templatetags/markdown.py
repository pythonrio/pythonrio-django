import re
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify
from django import template


register = template.Library()


@register.filter
def render_markdown(value):
    return markdownify(value)


@register.filter
def add_class(value, css_class):
    class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')
    string = value
    match = class_re.search(string)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class), match.group(1))
        if not m:
            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                                          string, 1))
    else:
        return mark_safe(string.replace('>', ' class="%s">' % css_class, 1))
    return value
