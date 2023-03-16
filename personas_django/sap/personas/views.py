from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


# Create your views here.
def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

# PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')

    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def borrarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

# CRUD de domicilio
def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilio/detalle.html', {'domicilio': domicilio})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')

    else:
        formaDomicilio = DomicilioForm()

    return render(request, 'domicilio/nuevo.html', {'formaDomicilio': formaDomicilio})

def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request, 'domicilio/editar.html', {'formaDomicilio': formaDomicilio})

def borrarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('index')



