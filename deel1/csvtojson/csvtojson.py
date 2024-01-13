import sys
import csv
import json
import requests
pokemon = []


def csvtojson():
    pad = sys.argv[1]
    with open(f'{pad}', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=' ')
        for row in reader:
            gen = row["Generation"]
            if gen == '2':
                pokemon.append(row)
    with open('test.json', 'w') as jsonfile:
        json.dump(pokemon, jsonfile, indent=2)


csvtojson()
