#Central Park Squirrel Data Analysis

import pandas

data = pandas.read_csv("/home/veggiedev/Curso-Python/Udemy_Python/day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(f'Grey Sqirrels:  {grey_squirrels_count}.')
print(f'Red Squirrels: {red_squirrels_count}.')
print(f'Black Squirrels: {black_squirrels_count}.')

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
