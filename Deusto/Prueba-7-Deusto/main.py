###################################imports###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sqlite3

#######################trabajo de pagina con selenium################################

website = "https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#Canciones_con_m%C3%A1s_semanas_en_el_n%C3%BAmero_uno"
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(website)
data = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody')
#extraemos columnas de la tabla
col1 = data.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[1]')
col2 = data.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[2]/a[1]')
col3 = data.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[3]')
col4 = data.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[4]')
col5 = data.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[5]')

#tema
col1_list = []
#interprete
col2_list = []
#anyo
col3_list = []
#semanas
col4_list = []
#pais
col5_list = []
#idioma
col6_list = ['Español', 'Español', 'Ingles', 'Español', 'Español', 'Ingles', 'Español', 'Ingles y Español', 'Ingles', 'Ingles', 'Ingles', 'Español', 'Portugues', 'Ingles', 'Español', 'Portugues', 'Español', 'Ingles', 'Español', 'Ingles', 'Español', 'Ingles', 'Español', 'Ingles']
#continente
col7_list = ['America del Sur', 'America del Sur', 'America del Norte', 'Europeo', 'Europeo', 'America del Sur', 'America del Sur', 'America del Sur', 'America del Sur', 'America del Norte', 'Europeo', 'America del Sur', 'America del Sur', 'Europeo', 'America del Sur', 'America del Sur', 'Europeo', 'Europeo', 'America del Sur', 'Europeo', 'America del Sur', 'Europeo', 'Europeo', 'Europeo']
#convertimos las columnas en listas
for item in col1:
    col1_list.append(item.text)
for item in col2:
    col2_list.append(item.text)
#guardamos solo los 4 primeros caracteres de cada entry en lista col2_lista
col3_list_temp = []
for item in col3:
    col3_list_temp.append(item.text)
for item in col4:
    col4_list.append(item.text)
for item in col5:
    col5_list.append(item.text)
#columna fecha revisada
for item in col3_list_temp:
    col3_list.append(item[0:4]) 

tabla_tuples =  []

tabla_listas = [col1_list, col2_list, col3_list, col4_list, col5_list, col6_list, col7_list]

for i in range(24):
    row = []
    for col in tabla_listas:
        row.append(col[i])    
    row_tuple = tuple(row)        
    tabla_tuples.append(row_tuple)

####################################base de datos#######################################

conn = sqlite3.connect('bd_canciones.db')
cursor = conn.cursor()

#########EJECUTAR UNA VEZ PARA SACAR DATOS DE LA PAGINA A LA BASE DE DATOS###########

cursor.execute('CREATE TABLE IF NOT EXISTS numeros1 (tema, interprete, fecha, semanas, pais, idioma, continente)')
for tuple in tabla_tuples:
     cursor.execute('INSERT INTO numeros1 VALUES(?,?,?,?,?,?,?)', tuple)

conn.commit()

cursor.execute('SELECT * FROM numeros1')
lineas = cursor.fetchall()
for entry in lineas:
    print(entry)

driver.quit()
######################################UI################################################
numero_preguntas = [1, 2, 3, 4, 5, 6]
game_on = True
def limpiar_str(str):
    return str.replace(" ", "")
while game_on:
    lista_preguntas = ['###Canciones con más semanas en el número uno###', 
                        '1.¿Cuál es la canción más antigua de la lista?', 
                        '2.¿Qué artista aparece más veces en esta lista?', 
                        '3.¿Qué país tiene más artistas en esta lista?', 
                        '4.¿Cuantas canciones distintas hay por cada idioma?', 
                        '5.¿Cuál es el continente con más apariciones en la lista?', 
                        '6.¿Qué canción ha estado más % de tiempo al año como número 1?']
    for pregunta in lista_preguntas:
        print(pregunta)
    try:
        pregunta = int(input('Elige la opcion del 1 al 6 o escribe 0 para salir: '))
    except:
        ValueError
        print('-------Introduce un numero del 1 al 6 por favor-------')
    if pregunta == 0:
        game_on = False
    elif pregunta not in numero_preguntas:
        print('Por favor, elija una opcion del 1 al 6')
    elif pregunta == 1:
        lista_fechas = cursor.execute('SELECT fecha FROM numeros1')
        min_fecha = min(lista_fechas)
        def cancion_antigua():
            cursor.execute('SELECT tema FROM numeros1 WHERE fecha=?', min_fecha)
            imp_cancion = cursor.fetchall()
            for registro in imp_cancion:
                print(f'\nHas elegido {lista_preguntas[pregunta]}')
                print(f'\n{registro[0]}\n')
        cancion_antigua()
    elif pregunta == 2:
        contador = 0
        mas_veces = cursor.execute('SELECT interprete FROM numeros1')
        lista_bd = cursor.fetchall()
        lista_interpretes = []
        for i in lista_bd:
            lista_interpretes.append(i)   
        lista_no_rep = lista_interpretes[0] 
        for cantante in lista_interpretes:
            frecuencia = lista_interpretes.count(cantante)
            if(frecuencia > contador):
                contador = frecuencia
                lista_no_rep = cantante
        print(f'\nHas elegido {lista_preguntas[pregunta]}')
        print(f'\n{lista_no_rep[0]}\n')
    elif pregunta == 3:
        contador_pais = 0
        mas_veces = cursor.execute('SELECT pais FROM numeros1')
        lista_bd_pais = cursor.fetchall()
        lista_paises = []
        for i in lista_bd_pais:
            lista_paises.append(i) 
        # print(lista_paises)  
        lista_no_rep_paises = lista_paises[0] 
        for cada_pais in lista_paises:
            frecuencia_paises = lista_paises.count(cada_pais)
            if(frecuencia_paises > contador_pais):
                contador_pais = frecuencia_paises
                lista_no_rep_paises = cada_pais
                pais = limpiar_str(lista_no_rep_paises[0])
        print(f'\nHas elegido {lista_preguntas[pregunta]}')
        print(f'\n{pais}\n')
    elif pregunta == 4:
        lista_idiomas = []
        lista_idiomas_no_rep = []
        idioma = cursor.execute('SELECT pais FROM numeros1')
        idiomas = idioma.fetchall()
        for i in idiomas:
            lista_idiomas.append(i)
        for id in lista_idiomas:
            if id not in lista_idiomas_no_rep:
                lista_idiomas_no_rep.append(id)
        print(f'\nHas elegido {lista_preguntas[pregunta]}')
        print(f'\n{len(lista_idiomas_no_rep)}\n')
    elif pregunta == 5:
        contador_cont = 0
        cont_veces = cursor.execute('SELECT continente FROM numeros1')
        lista_cont = cursor.fetchall()
        lista_de_continentes = []
        for i in lista_cont:
            lista_de_continentes.append(i)   
        lista_no_rep_cont = lista_de_continentes[0] 
        for cont in lista_de_continentes:
            frecuencia_cont = lista_de_continentes.count(cont)
            if(frecuencia_cont > contador_cont):
                contador_cont = frecuencia_cont
                lista_no_rep_cont = cont
        print(f'\nHas elegido {lista_preguntas[pregunta]}')
        print(f'\n{lista_no_rep_cont[0]}\n')
    elif pregunta == 6:
        lista_semanas = []
        max_semanas = 0
        semanas_anyo = cursor.execute('SELECT semanas FROM numeros1')
        semanas = semanas_anyo.fetchall()
        for semana in semanas:
            lista_semanas.append(semana)
        for i in lista_semanas:
            if int(i[0]) > max_semanas:
                max_semanas = int(i[0])
        porcentaje = (max_semanas / 52)*100
        
        cancion_semanas = cursor.execute('SELECT tema FROM numeros1 ORDER BY semanas DESC LIMIT 1')
        for i in cancion_semanas:
            lista_semanas = i[0]
        print(f'\nHas elegido {lista_preguntas[pregunta]}')
        print(f'\n"{lista_semanas}" con un {round(porcentaje, 2)}% del año\n')
        