import tkinter
import pandas
import random
import sqlite3
from pathlib import Path



#create nombres.csvv
nombres_txt = open('BuscoAmigos/names.txt').readlines()
nombres = [i.removesuffix('\n') for i in nombres_txt]
#create apellidos.csv
apellidos_bd = pandas.read_csv("BuscoAmigos/apellidos.csv")
apellidos_caps = apellidos_bd['apellido'].to_list()
apellidos = [i.capitalize() for i in apellidos_caps]
#create ciudades.csv
ciudades_csv = pandas.read_csv("BuscoAmigos/municipios.csv")
todas_ciudades = ciudades_csv['Municipio2'].to_list()
ciudades = [] 
for i in range(5000):
    ciudad = random.choice(todas_ciudades)
    if ciudad not in ciudades:
        ciudades.append(ciudad)
    else:
        continue
#posible answers to profiling questions
genero = ['hombre', 'mujer']
p1 = ['piña','no piña']
p2 = ['comida rápida', 'restaurante']
p3 = ['relajada', 'rápida']
p4 = ['pop', 'hip hop']
p5 = ['rock/metal', 'techno']
p6 = ['disco', 'bar']
p7 = ['montaña', 'playa']



# [(1, 'pokerkid'), (2, 'crazyken')]uscoAmigos/usuarios.csv")

#nombre,edad,genero,ciudad,pizza,burger,lugar_comida,musica,mus_relajada,mus_rapida,salir,actividades

'''Create dummy db'''
# all__full_names = []
# all_edades = []
# all_generos = []
# all_ciudades = []
# all_pizza = []
# all_burger = []
# all_restaurante = []
# all_musica = []
# all_relajada = []
# all_rapida = []
# all_salir = []
# all_actividades = []

# for i in range (5000):
#     rand_full_name = random.choice(nombres) + ' ' + random.choice(apellidos)
#     rand_edad = random.randint(18, 50)
#     rand_genero = random.choice(genero)
#     rand_ciudad =  random.choice(ciudades)   
#     rand_pizza = random.choice(p1)from pathlib import Path

#     rand_mus_relajada = random.choice(p4)
#     rand_mus_rapida = random.choice(p5)
#     rand_salir = random.choice(p6)
#     rand_actividades = random.choice(p7)

#     all__full_names.append(rand_full_name)
#     all_edades.append(rand_edad)
#     all_generos.append(rand_genero)
#     all_ciudades.append(rand_ciudad)
#     all_pizza.append(rand_pizza)
#     all_burger.append(rand_burger)
#     all_restaurante.append(rand_lugar_comida)
#     all_musica.append(rand_musica)
#     all_relajada.append(rand_mus_relajada)
#     all_rapida.append(rand_mus_rapida)
#     all_salir.append(rand_salir)
#     all_actividades.append(rand_actividades)

# rand_user_data = {
#     'nombre': all__full_names,
#     'edad': all_edades,
#     'genero': all_generos,
#     'ciudad': all_ciudades,
#     'pizza': all_pizza,
#     'burger': all_burger,
#     'lugar_comida': all_restaurante,
#     'musica': all_musica,
#     'mus_relajada': all_relajada,
#     'mus_rapida': all_rapida,
#     'salir': all_salir,
#     'actividades': all_actividades,
# }

# df = pandas.DataFrame(rand_user_data)

# df.to_csv('BuscoAmigos/usuarios.csv', mode='a', index=False, header=False)

Path('usuarios_bd.db').touch()

conn = sqlite3.connect('usuarios_bd.db')
c = conn.cursor()
# c.execute('''CREATE TABLE usuarios (nombre,edad,genero,ciudad,pizza,burger,lugar_comida,musica,mus_relajada,mus_rapida,salir,actividades)''')

usuarios = pandas.read_csv('BuscoAmigos/usuarios.csv')

usuarios.to_sql('usuarios', conn, if_exists='append', index=False)

c.execute('''SELECT * FROM usuarios''').fetchall() 



# print(apellidos)
# apellidos = 

# lista_de_apellidos = []
# lista_apellidos = [lista_de_apellidos.append(i) for i in apellidos_bd.apellido()]
# print(lista_de_apellidos)




# print(bd)