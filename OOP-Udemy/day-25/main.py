
# data = []

# with open('OOP-Udemy/day-25/weather_data.csv') as weather:
#     data_weather = weather.readlines()
    
# for data_entry in data_weather:
#     data.append(data_entry)
    
# print(data)

import csv


    
import pandas

data = pandas.read_csv('OOP-Udemy/day-25/weather_data.csv')

data_dict = data.to_dict()
max_temp = data.temp.max() 
print(max_temp)

for i in data_dict:
    if max_temp in i:
        print(i)
# print(data_dict)



for row in data['temp']:
    if row == max_temp:
        print(row['condition'])
        # if row[1] == max_temp:
        #     print(row)
    
# temp_list = data['temp'].to_list()

# print(temp_list)
# total_numbers = 0
# for num in temp_list:
#     total_numbers += num
# average = round(total_numbers / len(temp_list), 1)

highest_temp = 0

# for data_entry in data:
#     print(data_entry)
#     if data_entry.temp > highest_temp:
#         data_entry.temp = highest_temp
#     if highest_temp == data_entry.temp:
#         print(data_entry)
# # data['temp'].max()