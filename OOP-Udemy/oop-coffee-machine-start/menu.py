class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working... ")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
         super().__init__(name, age, salary)
         self.level = level
class Designer(Employee):
    def __init__(self, name, age, salary):
         super().__init__(name, age, salary)
    pass

se = SoftwareEngineer('Bob', 32, 5000, 'Senior Engineer')

de = Designer('Brian', 43, 4000)


# class Colegio:
#     def __init__(self, nombre_cole):
#         self.nombre_cole = nombre_cole
#     clases = ['1A', '1B', '2A', '2B']


# class Gente(Colegio):
#     def __init__(self, nombre, edad, nombre_cole, clase):
#         self.nombre = nombre
#         self.edad = edad
#         super().__init__(nombre_cole)
#         self.clase = clase

        

# class Profesor(Gente):
#     def __init__(self, nombre, edad, nombre_cole, clase, materia):
#         super().__init__(nombre, edad, nombre_cole, clase)
#         self.materia = materia

# class Alumno(Gente):
#     def __init__(self, nombre, edad, nombre_cole, clase):
#         super().__init__(nombre, edad, nombre_cole, clase)

# prof1 = Profesor('Brian Cox', 58, 'Txomin Aguirre', Colegio.clases[1], 'Ciencias')
# alu1 = Alumno('Tony Stark', 32, 'Txomin Aguirre', Colegio.clases[0])
# print(prof1.clase)
# print(alu1.clase)




#print(Colegio.clases[0])