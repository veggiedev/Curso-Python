# with open("/Users/veggiedev/Curso-Python/OOP-Udemy/Turtle Exercises/day24/my_file.txt") as file:

#     contents = file.read()

#     print(contents)

with open("new_file", mode='w') as file:
    file.write("New file.")