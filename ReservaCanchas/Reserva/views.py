from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Cancha
from .models import Persona

# Create your views here.
def getInfoCanchaById(request, id_cancha):
    cancha = Cancha.objects.get(id=id_cancha)
    result = f"Cancha: {cancha.nombre}, Descripción: {cancha.descripcion}, Precio: {cancha.costo_por_hora}"
    return HttpResponse(result) 

def getInfoPersonaId(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    result = f"Nombre: {persona.nombre}, Apellido: {persona.apellido}, Cedula: {persona.cedula}"
    return HttpResponse(result) 

def getInfoPersonaCed(request, ced_persona):
    persona = Persona.objects.get(cedula=ced_persona)
    result = f"Nombre: {persona.nombre}, Apellido: {persona.apellido}, Email: {persona.correo}"
    return HttpResponse(result) 

