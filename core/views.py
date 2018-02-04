from datetime import datetime
from django.shortcuts import render

from core.models import Evento


def index(request):
    eventos = Evento.objects.filter(data__gte=datetime.now())
    return render(request, 'index.html', {'eventos': eventos})


def eventos(request):
    evento_atual = Evento.objects.latest('id')
    context = {
        'evento_atual': evento_atual
    }
    return render(request, 'eventos.html', context)
