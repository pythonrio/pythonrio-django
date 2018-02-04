from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


from core.models import Evento, Parceiro

admin.site.register(Evento, MarkdownxModelAdmin)
admin.site.register(Parceiro)
