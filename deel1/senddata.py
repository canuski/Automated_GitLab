import json
import requests


def sendData():
    voornaam = input("Geef je voornaam: ")
    achternaam = input("Geef je achternaam: ")
    data = {'voornaam': voornaam, 'achternaam': achternaam}
    antwoord = requests.post('https://httpbin.org/post', data=data)
    print(f'Statuscode: {antwoord.status_code}')


sendData()
