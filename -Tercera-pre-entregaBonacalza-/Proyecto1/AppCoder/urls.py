from django.urls import path

from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('sub', views.sub, name="Sub"),
    path('moto', views.moto, name="Motos"),
    path('dep', views.autodep, name="Autosdep"),
    path('depFormulario', views.deportivoFormulario, name="DepFormulario"),
    path('subFormulario', views.subFormulario, name="SubFormulario"),
    path('motoFormulario', views.motoFormulario, name="MotoFormulario"),
    path('busquedaAutos', views.busquedaAutos, name="BusquedaAutos"),
    path('buscar/', views.buscar),
]