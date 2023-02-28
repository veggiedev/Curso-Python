import pandas as pd
import random
import sqlite3



logged_in_user = 'Juaquin Consejero'
random


conn = sqlite3.connect('templates/buscoAmigosApp/usuarios_bd.db')
c = conn.cursor()
# ciudades = c.execute("SELECT * FROM usuarios WHERE ciudad = 'Ceuta'").fetchall() 
# # for row in ciudades:
# #     print(row)



ciudad = 5
disponibilidad = 6
lugar_comida = 7
musica = 8
mus_relax = 9
mus_rapida = 10
salir = 11
actividades = 12
latitud = 14
longitud = 15


usuario_1 = c.execute(f"SELECT * from usuarios WHERE nombre = '{logged_in_user}'").fetchone()
# usuario_1_ciudad = [usuario_1[ciudad]]




lista_usuarios = c.execute("SELECT * from usuarios").fetchall()
lista_nombres = []
for row in lista_usuarios:
    lista_nombres.append(row[0])


usuarios_locales = c.execute(f"SELECT * from usuarios WHERE ciudad = '{usuario_1[ciudad]}'").fetchall()
usuarios_locales_list = {}
# for user in usuarios_locales:
#     print(user)

usuario_random = random.choice(usuarios_locales)
print(usuario_random)







# df = pd.DataFrame('templates/buscoAmigosApp/usuarios_bd.db')
# print(df)



# usuario_2 = c.execute(f" SELECT from usuarios WHERE nombre = '{usuario_random}'")
# if usuario_1[ciudad] == usuario_2[ciudad]:
#     print('Match!')


# print(usuarios_1_gustos)




# user_names = c.execute("SELECT nombre FROM usuarios").fetchall() 
# for row in user_names:
#     print(row)

# user_1 = c.execute("SELECT pizza,lugar_comida,musica,mus_relajada,mus_rapida,salir,actividades,latitud,longitud FROM  usuarios WHERE nombre = 'logged_in_user'", conn).fetchall()
# for row in user_1:
#     print(row)