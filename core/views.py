from django.shortcuts import render

from core.models import Evento


def index(request):
    eventos = Evento.objects.all()
    return render(request, 'index.html', {'eventos': eventos})


def eventos(request):
    eventos = Evento.objects.all()
    evento_atual = Evento.objects.latest('id')
    context = {
        'eventos': eventos,
        'evento_atual': evento_atual
    }
    return render(request, 'eventos.html', context)
