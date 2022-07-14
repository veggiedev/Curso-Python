class Guitarra:

    #contructor de clases

    def __init__(self, nombre, cuerdas, afinacion, color, enchufable):
        self.nombre = nombre
        self.cuerdas = cuerdas
        self.afinacion = afinacion
        self.color = color
        self.enchufable = enchufable
        print('Se ha creado el instrumento:', self.nombre)

        #Redefinimos e; metodo str de la clase
        def __str__(self):
            return '{} ({})'.format(self.nombre, self.color)

class Coleccion:
    guitarras = []
    #El contructor toma el objeto self y una lista vacia
    def __init__(self, guitarras=[]):
        self.guitarras = guitarras

    def agregar(self, g):
        self.guitarras.append(g)

    def mostrar(self):
#        for g in self.guitarras:
        print(self.guitarras)
g = Guitarra("Washburn", 6, "mi", "Negro", True)
c = Coleccion([g]) #Anyado una lista con una guitarra a traves del constructor de clase
c.mostrar()
c.agregar(Guitarra("Epiphone", 6, "mi", "Ocre", True))
c.mostrar()

guitarrass = Coleccion
print(guitarrass.guitarras)


# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
# machine = CoffeeMaker()
# menu_items = Menu()
# print(menu_items.get_items())
# print(machine.resources['water'])

# # list_of_items = ["1-Espresso", "2-Latte", "3-Capuccino"]
# # print(list_of_items)
# order_name = input("What would like? ")
# find_the_drink = menu_items.find_drink(order_name)
# if order_name == "report":
#     print("User has selected 'report'")
#     print(machine.report())
# #elif order_name == "menu":
# elif order_name == "espresso":
# # #    find_the_drink
#     print(menu_items[0])
# #     print(latte)
