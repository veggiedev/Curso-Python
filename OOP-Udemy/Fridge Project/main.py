class Fridge:
    def __init__(self, vegetables, dairy, door):
        self.vegetables = vegetables
        self.dairy = dairy
        self.door = door

my_fridge = Fridge( {"vegetables":{"tomatoes":5,"oranges":6,"cucumber":1}},
                    {"dairy":{"yogurts":5,"cheese":1,"milk":500,"eggs":12}}, 
                    {"door": ["coke", "fanta_orange", "water"]})

# print(my_fridge.vegetables)

# # class Omelette:
# #     def __init__(self, ingredients):
# #         self.ingredients = ingredients

my_omelette = {"ingredients":{"eggs":8, "milk":150}}

# print(my_omelette)
# print(my_fridge.dairy)

meal = input("What's for dinner? ")
leftovers = {}
#print(type(my_omelette.value))
#print(my_omelette["ingredients"])
if meal == "omelette":
    for item in my_omelette["ingredients"]:
        print(item)
        #print(my_fridge.dairy["dairy"])
        if item in my_fridge.dairy[item]:

            my_fridge.dairy[item] -= my_omelette[item]
            print("We have a match")

        # if (item in my_fridge.dairy["dairy"] and my_omelette["ingredients"[item]] == my_fridge.dairy["dairy"[item]]):
        #     print(item)
        #     my_fridge.dairy["dairy"][item.value] -= my_omelette["ingredients"][item.value]
        else:
            pass
    print(my_fridge.dairy)


