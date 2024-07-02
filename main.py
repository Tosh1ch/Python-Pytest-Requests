import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a08e0d74b44975e87477ea2d002bb0fe'
HEADER = {'Content-type' : 'application/json','trainer_token':TOKEN}

body_create = {
    "name": "Yatoro",
    "photo_id": 903
}

body_rename = {
    "pokemon_id": "39617",
    "name": "Miposhka",
    "photo_id": 908
}

body_catch = {
    "pokemon_id": "39617"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

'''response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)'''
