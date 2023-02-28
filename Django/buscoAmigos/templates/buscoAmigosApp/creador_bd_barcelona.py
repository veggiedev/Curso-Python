import pd as pd
import random
import sqlite3
import os
from pathlib import Path
from geopy.geocoders import Nominatim
import geopy.distance 
import time






dir_path = r'/home/veggiedev/Downloads/provincias_excel/'
lista_provs = []



# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        lista_provs.append(path.removesuffix('.xls'))
provincias_ordenadas = sorted(lista_provs)
# print(provincias_ordenadas)


'''----------------crea una provincia y municipio aleatorio----------------'''

barcelona = pd.read_csv(f'/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/provincias/barcelona.csv')
# print(random_provincia.capitalize())
lista_municipios = barcelona.NOMBRE.to_list()
# random_municipio = random.choice(lista_municipios)
print(lista_municipios)

# # nombre : create list of nombres nombres
nombres_txt = open('/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/names.txt').readlines()
nombres = [i.removesuffix('\n') for i in nombres_txt]

# #open apellidos.csv then create a list of apellidos
apellidos_bd = pd.read_csv("/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/apellidos.csv")
apellidos_caps = apellidos_bd['apellido'].to_list()
apellidos = [i.capitalize() for i in apellidos_caps]




#posible answers to profiling questions
genero = ['hombre', 'mujer', 'otro','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre',
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer','hombre', 'mujer',
        'hombre', 'mujer','hombre', 'mujer','hombre', 
        'mujer','hombre', 'mujer']
p1_disponibilidad_dias = ['find de semana','estresemana']
p2_horarios = ['mañana', 'tarde', 'noche']
p3_salida_urbana = ['bar', 'disco']
p4_salida_naturaleza = ['playa', 'montaña']
p5_tipo_comida = ['rapida', 'restaurante']
p6_estilo_musical = ['disco', 'bar']
p7_mascotas = ['perros', 'gatos']
p8_actividad = ['netflix', 'salir', 'deporte']



# '''nombre,edad,genero,ciudad,provincia,
# 1-disponibilidad dias,2-horarios,3salida urbana,
# 4-salida naturaleza,5-tipo comida,6-estilo musical,
# 7-mascotas,8-nivel actividad'''

# '''Create dummy db'''
all__full_names = [] #nombre + apellido
all_edades = [] # random randint 
all_generos = [] # genero[]
all_provincias = []
all_ciudades = [] # ciudades
all_disponibilidad = [] # p1
all_horarios = [] #p2
all_salida_urbana = [] # p3 
all_salida_naturaleza = [] # p4 
all_tipo_comida = [] # p5 
all_estilo_musical = [] # p6
all_mascotas = [] # p7
all_actividad = [] # p8
all_photos = []
all_latitud = []
all_longitud = []
all_correo = []
passes = 0
# print(random_provincia.capitalize())
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Process started at ", current_time)

for i in range (1):
    for i in range (2):
        for i in range (50):
            rand_name = random.choice(nombres)
            rand_apellido = random.choice(apellidos)
            rand_full_name = rand_name + ' ' + rand_apellido
            rand_photo = (f'/templates/buscoAmigosApp/Images/{random.randint(1, 2031)}.jpg')
            all__full_names.append(rand_full_name)
            all_edades.append(random.randint(18, 99))
            all_correo.append(rand_name + rand_apellido +'@micorreo.es')
            all_generos.append(random.choice(genero))
            random_provincia = random.choice(provincias_ordenadas)
            all_provincias.append(random_provincia.capitalize())
            provincia_csv = pd.read_csv(f'templates/buscoAmigosApp/provincias/{random_provincia.lower()}.csv')
            lista_municipios = provincia_csv.NOMBRE.to_list()
            random_ciudad = random.choice(lista_municipios)
            all_ciudades.append(random_ciudad.capitalize())
            all_disponibilidad.append(random.choice(p1_disponibilidad_dias))
            all_horarios.append(random.choice(p2_horarios))
            all_salida_urbana.append(random.choice(p3_salida_urbana))
            all_salida_naturaleza.append(random.choice(p4_salida_naturaleza))
            all_estilo_musical.append(random.choice(p6_estilo_musical))
            all_mascotas.append(random.choice(p7_mascotas))
            all_actividad.append(random.choice(p8_actividad))
            all_photos.append(rand_photo)
            # Generar longitud y latitud municipio
            loc = Nominatim(user_agent="GetLoc")
            getLoc = loc.geocode(random_ciudad)
            all_latitud.append(getLoc.latitude)
            all_longitud.append(getLoc.longitude)
            time.sleep(5)
        time.sleep(60)
        passes += 250
        print(f"Added 250 more to the csv database. Total added:  {passes} of 500")
        print("Wait 60 seconds for next pass please. Total time to finish is around 0.5 hours")

    time.sleep(60)
rand_user_data = {
    'nombre': all__full_names,
    'edad': all_edades,
    'correo': all_correo,
    'genero': all_generos,
    'provincia': all_provincias,
    'ciudad': all_ciudades,
    'disponibilidad': all_disponibilidad,
    'horarios': all_horarios,
    'salida_urbana': all_salida_urbana,
    'salida_naturaleza': all_salida_naturaleza,
    'estilo_musical': all_estilo_musical,
    'mascotas' : all_mascotas,
    'actividad': all_actividad,
    'photo' : all_photos,
    'latitud' : all_latitud,
    'longitud': all_longitud,
    'negativos': [],
    'positivos': [],
}


df = pd.DataFrame(rand_user_data)

df.to_csv('/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/usuarios_barcelona.csv', mode='a', index=False, header=False)




# provincia_csv = pd.read_csv(f'buscoAmigos/templates/buscoAmigosApp/{random_provincia.lower()}.csv')
# print(random_provincia.capitalize())
# lista_municipios = provincia_csv.NOMBRE.to_list()
# random_municipio = random.choice(lista_municipios)
# print(random_municipio)


