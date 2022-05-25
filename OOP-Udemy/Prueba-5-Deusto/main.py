from gustos import Gustos
from datos_personales import DatosPersonales
lista_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nombre = input("Nombre y apellidos: ").title()
lista_dni = []
dni = input('DNI: ')
while len(dni) != 9:
    print('El DNI debe contener 9 numeros y una letra al final')
    dni = input('DNI: ')
for letter in dni:
    lista_dni.append(letter)
if lista_dni[8].capitalize() not in lista_abc:
    print('Por favor, introduzca bien su DNI')
    dni = input('DNI: ')
else:
    pass 
          
poblacion = input('Poblacion: ').title()
pais = input('Pais: ').upper()

cancion = input('Cancion preferida: ').capitalize()
grupo = input(f'Por que grupo fue compuesta {cancion}? ').title()
estilo = input("Cual es el estilo musical? ").upper()



class TodosDatos(DatosPersonales, Gustos):    
    def imp_todos_datos(self):
        print(f'Nombre:{self.nombre}, DNI: {self.dni}, Poblacion: {self.poblacion}. Pais: {self.pais}\nCancion Favorita: {self.cancion}, Grupo: {self.grupo} Estilo Musical: {self.estilo}') 

todos_datos = TodosDatos()
todos_datos.nombre = nombre
todos_datos.dni = dni
todos_datos.poblacion = poblacion
todos_datos.pais = pais
todos_datos.cancion = cancion
todos_datos.grupo = grupo
todos_datos.estilo = estilo

todos_datos.imp_todos_datos()



