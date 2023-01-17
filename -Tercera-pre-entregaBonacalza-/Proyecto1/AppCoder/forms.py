from django import forms

class depFormulario(forms.Form):
        Marca = forms.CharField()
        Modelo = forms.CharField()
        Color = forms.CharField()
        Puertas = forms.IntegerField()

class SubFormulario(forms.Form):
        Marca = forms.CharField()
        Modelo = forms.CharField()
        Color = forms.CharField()
        Puertas = forms.IntegerField()

class MotoFormulario(forms.Form):
        Marca = forms.CharField()
        Modelo = forms.CharField()
        Color = forms.CharField()
        Kilometros = forms.IntegerField()

