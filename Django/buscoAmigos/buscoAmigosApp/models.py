from django.db import models
from datetime import date
from django import forms
# Create your models here.



class User(models.Model):
    nombre_usuario = models.CharField(verbose_name=('Nombre'),max_length=264,unique=False)
    # nacimiento = models.DateField(null=True,verbose_name=('Fecha de nacimiento'),)
    fecha_creacion  = models.DateField(
        default=("YYYY-MM-DD"),
        verbose_name=('Fecha cuenta creada'),
        # auto_now_add=True,
    )
    email = models.EmailField(null=True,verbose_name=('Correo electronico'),max_length=264,unique=True)
    password = forms.CharField(max_length=50)
    # genero = models.CharField(null=True,verbose_name=('Genero'),max_length=64,unique=False)
    # provincia = models.CharField(null=True,verbose_name=('Provincia'),max_length=264, unique=False)
    # ciudad = models.CharField(null=True,verbose_name=('Ciudad'),max_length=264,unique=False)
    # disponibilidad = models.CharField(null=True,max_length=264,unique=False)
    # lugar_comida = models.CharField(null=True,max_length=264,unique=False)
    # musica = models.CharField(null=True,max_length=264,unique=False)
    # musica_relax = models.CharField(null=True,max_length=264,unique=False)
    # musica_animada = models.CharField(null=True,max_length=264,unique=False)
    # salir = models.CharField(null=True,max_length=264,unique=False)
    # actividades = models.CharField(null=True,max_length=264,unique=False)
    # latitud = models.CharField(null=True,max_length=264,unique=False)
    # longitud = models.CharField(null=True,max_length=264,unique=False)
    # activo = models.BooleanField(
    #     verbose_name= ('Active'),
    #     default=True)
    
    # def age(self):
    #     today = date.today.strftime("%d/%m/%Y")
    #     born = self.birthday
    #     rest = 1 if (today.month, today.day) < (born.month, born.day) else 0
    #     return today.year - born.year - rest
    
    def __str__(self):
        return self.nombre_usuario
    
# class Webpage(models.Model):
#     user_name = models.ForeignKey(User)
#     name = models.CharField(max_length=264,unique=False)

# peter = User()

# peter.nombre_usuario('Pete Smith')

# print(peter.nombre_usuario)