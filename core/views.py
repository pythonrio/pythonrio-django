from django.shortcuts import render

from core.models import Evento


def index(request):
    eventos = Evento.objects.all()
    return render(request, 'index.html', {'eventos': eventos})
