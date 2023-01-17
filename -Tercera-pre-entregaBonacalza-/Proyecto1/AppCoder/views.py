from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

def inicio(request):

      return render(request, "AppCoder/inicio.html")

def sub(request):

      return render(request, "AppCoder/autosub.html")

def moto(request):

      return render(request, "AppCoder/moto.html")


def autodep(request):

      return render(request, "AppCoder/autodep.html")

#########################
def busquedaAutos(request):
      return render(request, "AppCoder/busquedaAutos.html")

def buscar(request):
      if request.GET['marca']:
            marca = request.GET['marca']
            modelo = AutoDeportivo.objects.filter(marca__icontains=marca)
            color = AutoDeportivo.objects.filter(marca__icontains=marca)
            puertas = AutoDeportivo.objects.filter(marca__icontains=marca)
            return render(request, "AppCoder/resultadosBusqueda.html", {"Modelo": modelo,"Marca": marca,"Color": color,"Puertas": puertas})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse(respuesta)
######################
def deportivoFormulario(request):
      if request.method == "POST":
            miFormulario = depFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  auto = AutoDeportivo(marca=informacion["Marca"], modelo=informacion["Modelo"], color=informacion["Color"], puertas=informacion["Puertas"])
                  auto.save()
                  return render(request, "AppCoder/inicio.html")
      else: 
            miFormulario = depFormulario()
      return render(request, "AppCoder/depFormulario.html", {"miFormulario": miFormulario})

def subFormulario(request):
      if request.method == "POST":
            miFormulario = SubFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  auto = AutoSub(marca=informacion["Marca"], modelo=informacion["Modelo"], color=informacion["Color"], puertas=informacion["Puertas"])
                  auto.save()
                  return render(request, "AppCoder/inicio.html")
      else: 
            miFormulario = SubFormulario()
      return render(request, "AppCoder/subFormulario.html", {"miFormulario": miFormulario})

def motoFormulario(request):
      if request.method == "POST":
            miFormulario = MotoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  moto = Moto(marca=informacion["Marca"], modelo=informacion["Modelo"], color=informacion["Color"], puertas=informacion["Kilometros"])
                  moto.save()
                  return render(request, "AppCoder/inicio.html")
      else: 
            miFormulario = MotoFormulario()
      return render(request, "AppCoder/motoFormulario.html", {"miFormulario": miFormulario})