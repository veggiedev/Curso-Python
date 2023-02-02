import pandas
import random
import sqlite3
from pathlib import Path



#create list of nombres nombres
# nombres_txt = open('/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/names.txt').readlines()
# nombres = [i.removesuffix('\n') for i in nombres_txt]

# #open apellidos.csv then create a list of apellidos
# apellidos_bd = pandas.read_csv("/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/apellidos.csv")
# apellidos_caps = apellidos_bd['apellido'].to_list()
# apellidos = [i.capitalize() for i in apellidos_caps]



# #create ciudades.csv
# ciudades_csv = pandas.read_csv("/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/municipios.csv")
# todas_ciudades = ciudades_csv['Municipio2'].to_list()
# ciudades = [] 
# for i in range(5000):
#     ciudad = random.choice(todas_ciudades)
#     if ciudad not in ciudades:
#         ciudades.append(ciudad)
#     else:
#         continue

#convert image to binary data
# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         blobData = file.read()
#     return blobData

#numero de imagenes: 2032


#posible answers to profiling questions
# genero = ['hombre', 'mujer', 'otro']
# p1 = ['piña','no piña']
# p2 = ['comida rápida', 'restaurante']
# p3 = ['relajada', 'rápida']
# p4 = ['pop', 'hip hop']
# p5 = ['rock/metal', 'techno']
# p6 = ['disco', 'bar']
# p7 = ['montaña', 'playa']


# # [(1, 'pokerkid'), (2, 'crazyken')]uscoAmigos/usuarios.csv")

# #nombre,edad,genero,ciudad,pizza,comida,lugar_comida,musica,mus_relajada,mus_rapida,salir,actividades

# # '''Create dummy db'''
# all__full_names = [] #nombre + apellido
# all_edades = [] # random randint 
# all_generos = [] # genero[]
# all_ciudades = [] # ciudades
# all_pizza = [] # p1
# # all_comida = []
# all_restaurante = [] #p2
# all_musica = [] # p3
# all_relajada = [] # p4
# all_rapida = [] # p5
# all_salir = [] # p6
# all_actividades = [] # p7
# all_photos = []

# for i in range (5000):
#     rand_full_name = random.choice(nombres) + ' ' + random.choice(apellidos)
#     rand_edad = random.randint(18, 50)
#     rand_genero = random.choice(genero)
#     rand_ciudad =  random.choice(ciudades)   
#     rand_pizza = random.choice(p1)
#     rand_restaurante = random.choice(p2)
#     rand_musica = random.choice(p3)
#     rand_mus_relajada = random.choice(p4)
#     rand_mus_rapida = random.choice(p5)
#     rand_salir = random.choice(p6)
#     rand_actividades = random.choice(p7)
#     rand_photo = (f'/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/Images/{random.randint(1, 2031)}.jpg')
#     # rand_photo_bin = convertToBinaryData(rand_photo)

#     all__full_names.append(rand_full_name)
#     all_edades.append(rand_edad)
#     all_generos.append(rand_genero)
#     all_ciudades.append(rand_ciudad)
#     all_pizza.append(rand_pizza)
#     all_restaurante.append(rand_restaurante)
#     all_musica.append(rand_musica)
#     all_relajada.append(rand_mus_relajada)
#     all_rapida.append(rand_mus_rapida)
#     all_salir.append(rand_salir)
#     all_actividades.append(rand_actividades)
#     all_photos.append(rand_photo)

# rand_user_data = {
#     'nombre': all__full_names,
#     'edad': all_edades,
#     'genero': all_generos,
#     'ciudad': all_ciudades,
#     'pizza': all_pizza,
#     'lugar_comida': all_restaurante,
#     'musica': all_musica,
#     'mus_relajada': all_relajada,
#     'mus_rapida': all_rapida,
#     'salir': all_salir,
#     'actividades': all_actividades,
#     'photo' : all_photos,
# }

# df = pandas.DataFrame(rand_user_data)

# df.to_csv('/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/usuarios.csv', mode='a', index=False, header=False)
# print(df)


conn = sqlite3.connect('/home/veggiedev/Curso-Python/Django/buscoAmigos/usuarios_bd.db')
c = conn.cursor()
# c.execute('''CREATE TABLE usuarios (nombre,edad,genero,ciudad,pizza,lugar_comida,musica,mus_relajada,mus_rapida,salir,actividades,photo)''')

# usuarios = pandas.read_csv('/home/veggiedev/Curso-Python/Django/buscoAmigos/templates/buscoAmigosApp/usuarios.csv')

# usuarios.to_sql('usuarios', conn, if_exists='append', index=False)

# c.execute('''SELECT * FROM usuarios''').fetchall() 

# for row in c.execute("SELECT * FROM usuarios ORDER BY nombre"):
#     print(row)

pd_db = pandas.read_sql_query("SELECT * from usuarios", conn)

print(pd_db)

# print(apellidos)
# apellidos = 

# lista_de_apellidos = []
# lista_apellidos = [lista_de_apellidos.append(i) for i in apellidos_bd.apellido()]
# print(lista_de_apellidos)




# print(bd)