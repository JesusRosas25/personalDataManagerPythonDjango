from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from personas.forms import DomicilioForm
from personas.models import Domicilio
from personas.forms import PersonaForm
from personas.models import Persona


# Create your views here.
def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

#PersonaForm = modelform_factory(Persona,exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editar_persona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminar_persona(request,id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

def detalleDomicilio(request, id):
    #persona = Persona.objects.get(pk=id)
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio})

def editar_domicilio(request,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})

def eliminar_domicilio(request,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('domicilios')