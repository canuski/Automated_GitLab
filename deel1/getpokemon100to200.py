import json
import requests

url = (f"https://pokeapi.co/api/v2/pokemon?offset=100&limit=200")
data = requests.get(url)
pokemonData = json.loads(data.text)

teller = 0
for item in pokemonData:
    print("De pokemon die je hebt gekozen heeft volgende info:")
    print(f"Naam: {pokemonData['results'][teller]['name']}")
    teller += 1
