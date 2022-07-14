import pandas as pd
import requests, json


game_is_on = True

while game_is_on:
    what_club = input('Introduce la URL del archivo json, o escriba salir: ')
    if what_club == 'salir':
        game_is_on = False
    else:
        url = requests.get(what_club)
        text = url.text

        json_data = json.loads(text)
        country = json_data['clubs'][0]['country']
        print(country)
        count = 0
        teams = []
        for team in json_data['clubs']:
            count += 1
            # teams.append(team['name'], team['code'])
            print(team)
            team_name = team['name']

            with open(f'{country}.txt', 'a') as file:
                file.writelines(f'{team_name}\n')

        print(f'---El numero de equipos en esta liga es de {count}---')