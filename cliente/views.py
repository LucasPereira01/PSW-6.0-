from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render
from eventos.models import Certificado, Evento
# Create your views here.

def meus_certificados(request):
    certificados = Certificado.objects.filter(participante = request.user)
    if certificados.count() == 0:
             messages.add_message(request, constants.ERROR,
                             'Voce não possui Certificados Gerados.')
    return render(request, 'meus_certificados.html',{'certificados':certificados})


def meus_eventos(request):
    eventos = Evento.objects.filter(criador = request.user)
    if eventos.count() == 0:
             messages.add_message(request, constants.ERROR,
                             'Voce nao tem eventos Cadastrados.')
    
    return render(request,'meus_eventos.html',{'eventos':eventos})