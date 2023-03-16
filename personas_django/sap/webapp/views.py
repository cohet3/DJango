from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona, Domicilio


# Create your views here.
def bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas,
                                               'no_domicilios': no_domicilios, 'domicilios': domicilios})
