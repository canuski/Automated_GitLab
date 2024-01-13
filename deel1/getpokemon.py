import json
import requests
pokemon = input("Geef de naam van de pokemon: ")
url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")
data = requests.get(url)
pokemonData = json.loads(data.text)
print("De pokemon die je hebt gekozen heeft volgende info:")
print(f"Naam: {pokemonData['name']}")
print("Abilities:")
for item in pokemonData['abilities']:
    ability_name = item['ability']['name']
    print(f" - {ability_name}")
print(f"Height: {pokemonData['height']}")
print(f"Weight: {pokemonData['weight']}")
print(f"Id: {pokemonData['id']}")
print("Moves:")
for item in pokemonData['moves']:
    move_name = item['move']['name']
    print(f" - {move_name}")
print("Stats")
for item in pokemonData['stats']:
    stat_name = item['stat']['name']
    stat_info = item['base_stat']
    print(f" - {stat_name} {stat_info}")
