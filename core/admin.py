from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


from core.models import Evento

admin.site.register(Evento, MarkdownxModelAdmin)
