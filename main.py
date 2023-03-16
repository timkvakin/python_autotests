import requests

token = '916e61cb1cc7fedb5377b34b74ba6491'
create_pok = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token' : token}, json={
    "name": "Рукожоп",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})
print(create_pok.text)
change_pok = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', 'trainer_token' : token}, json={
    "pokemon_id": "6223",
    "name": "Консерва",
    "photo": "https://dolnikov.ru/pokemons/albums/069.png"
})
print(change_pok.text)

catch_pok_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type': 'application/json', 'trainer_token' : token}, json={
    "pokemon_id": "6225"
})
print(catch_pok_pokeball.text)
