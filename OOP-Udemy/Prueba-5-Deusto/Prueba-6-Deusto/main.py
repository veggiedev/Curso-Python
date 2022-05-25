import pandas as pd
import json, requests

what_club = input('Introduce la URL del archivo json')
url = requests.get(what_club)
text = url.json

data = json.load(text)
count = 0
for key, value in data.items():
    if isinstance(value, list):
        count = len(value)
        print(value)
print(count)  
print(len(data['clubs']))
#     print(data['clubs'])
# # club_json = pd.read_json('OOP-Udemy/Prueba-5-Deusto/Prueba-6-Deusto/es.1.clubs.json')

# # print(club_json)

