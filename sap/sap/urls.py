"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personas.views import eliminar_domicilio
from personas.views import nuevoDomicilio
from personas.views import editar_domicilio
from personas.views import detalleDomicilio
from personas.views import eliminar_persona
from personas.views import nuevaPersona
from personas.views import detallePersona
from personas.views import editar_persona
# from webapp.views import contacto
# from webapp.views import despedirse
from webapp.views import bienvenido
from webapp.views import domicilios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editar_persona),
    path('eliminar_persona/<int:id>', eliminar_persona),
    path('domicilios', domicilios),
    path('detalle_domicilio/<int:id>', detalleDomicilio),
    path('nuevo_domicilio', nuevoDomicilio),
    path('editar_domicilio/<int:id>', editar_domicilio),
    path('eliminar_domicilio/<int:id>', eliminar_domicilio),
    # path('despedida.html', despedirse),
    # path('contacto', contacto)
]
