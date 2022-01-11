# class Fridge:
#     def __init__(self):
#         self.vegetables = {"tomatoes":5,"oranges":6,"cucumber":1}
#         self.dairy = {"yogurts":5,"cheese":1,"milk":500,"eggs":12}
#         self.drinks = ["coke", "fanta_orange", "water"]












# my_fridge = Fridge()

# # print(my_fridge.vegetables)

# # # class Omelette:
# # #     def __init__(self, ingredients):
# # #         self.ingredients = ingredients

# my_omelette = {"eggs":8, "milk":150}

# # print(my_omelette)
# # print(my_fridge.dairy)

# meal = input("What's for dinner? ")
# leftovers = {}
# #print(type(my_omelette.value))
# #print(my_omelette["ingredients"])








# if meal == "omelette":
#     for item in my_omelette:
#         print(item)
#         #print(my_fridge.dairy["dairy"])
#         if item in my_fridge.dairy:
#             my_fridge.dairy[item] -= my_omelette[item]
#             print("We have a match")

#         # if (item in my_fridge.dairy["dairy"] and my_omelette["ingredients"[item]] == my_fridge.dairy["dairy"[item]]):
#         #     print(item)
#         #     my_fridge.dairy["dairy"][item.value] -= my_omelette["ingredients"][item.value]
#         else:
#             pass
#     print(my_fridge.dairy)


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
       x_diff_sq = (self.x-other.x)**2
       x_diff_sq = (self.y-other.y)**2
    def __str__(self):
        return "<"+str(self.x) + ","+str(self.y)+">"
    
c = Coordinate(3, 4)
zero = Coordinate(0, 0)
print(c.distance(zero))
print(c)
print(isinstance(c, Coordinate))