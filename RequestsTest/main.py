
import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'e0c88f67f587becb93e7c7300c8b6b5d'
HEADERS = {'Content-Type' : 'application/json',  'trainer_token': TOKEN}

#создание покемона
'''body = {

    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/003.png"

}
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)''' 

#смена имени
'''body = {
    "pokemon_id": "16378",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)'''

#поймать в покебол
body = {
    "pokemon_id": "16378",
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)





 