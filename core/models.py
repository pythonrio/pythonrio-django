from datetime import datetime

from django.db import models
from markdownx.models import MarkdownxField

AGENDA_DEFAULT = '''Hora | Local | Atividade
--- | --- | ---
13:30|Recepção|Credenciamento
13:55||Abertura
14:00||
14:50||
15:40||
16:00||
16:30||
17:00||
17:50||Encerramento
18:00|No bar mais próximo, vamos trocar ideias e beber um chopp.|Pós-evento'''


class Parceiro(models.Model):
    logo_url = models.URLField()
    link = models.URLField()
    nome = models.CharField(max_length=255)

    def __str__(self):
        return 'Parceiro: {}'.format(self.nome)


class Evento(models.Model):
    nome = models.CharField(max_length=255, default="PythOnRio")
    descrição = MarkdownxField()
    endereço = models.CharField(max_length=255)
    agenda = MarkdownxField(default=AGENDA_DEFAULT)
    meetup_link = models.URLField(null=True, blank=True)
    palestras_link = models.URLField(null=True, blank=True)
    data = models.DateTimeField()
    data_fechamento_palestras = models.DateTimeField(null=True, blank=True)
    local = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255, default="Riode Janeiro")
    parceiros = models.ManyToManyField(Parceiro, blank=True)

    @property
    def palestras_estao_fechadas(self):
        return self.data_fechamento_palestras < datetime.now()
