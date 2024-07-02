import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a08e0d74b44975e87477ea2d002bb0fe'
HEADER = {'Content-type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID = '4596'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
def test_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Арктур'