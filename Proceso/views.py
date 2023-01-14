# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Vehiculo
from .forms import VehiculoForm #vista formulario
#from .forms import SelectForm
# Create your views here.

def principal(request):
   return render(request,'paginas/principal.html')
def vehiculos(request):
   vehiculos=Vehiculo.objects.all()
   return render(request,'vehiculos/index.html', {'vehiculos':vehiculos})
def crear(request):   
   formulario=VehiculoForm(request.POST or None, request.FILES or None)
   if formulario.is_valid():
      formulario.save()
      return redirect('vehiculos')
   return render(request,'vehiculos/crear.html', {'formulario':formulario})
def editar(request,id):
   vehiculo=Vehiculo.objects.get(id=id)
   formulario=VehiculoForm(request.POST or None, request.FILES or None, instance=vehiculo)
   if formulario.is_valid() and request.POST:
      formulario.save()
      return redirect('vehiculos')
   return render(request,'vehiculos/editar.html', {'formulario':formulario})
def eliminar(request,id):
   vehiculo=Vehiculo.objects.get(id=id)
   vehiculo.delete()
   return redirect('vehiculos')
