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


class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0
    
    def code(self):
        self._num_bugs_solved += 1
    
    def get_salary(self):
        if self._salary == None:
            print("You haven't specified a valid amount yet.")
        else:
            print(self._salary)
    
    global set_your_salary
    
    def set_salary(self, set_your_salary):
        if set_your_salary < 1000:
            self._salary = 1000
        elif set_your_salary > 20000:
            print('You introduced an amount considered too high')  
        else:
            self._salary = set_your_salary

se = SoftwareEngineer('Max', 56)

while True:
    try:
        set_your_salary = int(input('Set your salary: '))
        se.set_salary(set_your_salary)
    except ValueError:
            print('Enter a valid amount please.')
            continue
    break




while True:
    ask_salary = input("Get your salary? Answer 'yes' or 'no' ")
    if ask_salary.lower() == 'yes':
        se.get_salary()
    elif ask_salary.lower() == 'no':
        print('OK')
    else:
        print('Enter a valid answer please.')
        continue
    break
        

#print(se.age, se.name, se._salary)