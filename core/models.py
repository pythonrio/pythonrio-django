from django.db import models


class Evento(models.Model):
    data = models.DateTimeField()
    local = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255, default="Rio de Janeiro")
