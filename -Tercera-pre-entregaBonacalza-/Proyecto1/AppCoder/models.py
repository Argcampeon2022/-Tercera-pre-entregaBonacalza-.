from django.db import models

# Create your models here.
class AutoSub(models.Model):
                marca= models.CharField(max_length=30)
                modelo= models.CharField(max_length=30)
                color= models.CharField(max_length=254)
                puertas= models.IntegerField()
                def __str__(self):
                    return f"Marca: {self.marca} - Modelo: {self.modelo} - Color: {self.color} - Puertas: {self.puertas}"
                
class AutoDeportivo(models.Model):
                marca= models.CharField(max_length=30)
                modelo= models.CharField(max_length=30)
                color= models.CharField(max_length=254)
                puertas= models.IntegerField()
                def __str__(self):
                    return f"Marca: {self.marca} - Modelo: {self.modelo} - Color: {self.color} - Puertas: {self.puertas}"

class Moto(models.Model):
              marca= models.CharField(max_length=30)
              modelo= models.CharField(max_length=30)
              color= models.CharField(max_length=254)
              puertas= models.IntegerField()
              def __str__(self):
                    return f"Marca: {self.marca} - Modelo: {self.modelo} - Color: {self.color} - Kilometros: {self.puertas}"
