
from django.http import HttpResponse
from django.shortcuts import render
from personas.models import Domicilio

from personas.models import Persona

# Create your views here.
def bienvenido(request):
    #return HttpResponse('Hola Mundo desde Django')
    # mensajes = {'msg1': 'Valor mensaje 1', 'msg2': 'Valor mensaje 2'}
    # return render(request, 'bienvenido.html', mensajes)
    no_personas = Persona.objects.count()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas':personas})

def domicilios(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'domicilios.html', {'no_domicilios': no_domicilios, 'domicilios': domicilios})



# def despedirse(request):
#     return HttpResponse('Despedida desde Django')

# def contacto(request):
#     return HttpResponse('Mail: jesusrosas2508@gmail.com \nNumero: 1122530675')