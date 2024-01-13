import requests
import json
import os
import git
import sys


def list_groepen(token):
    # Functie om alle groepen op te lijsten
    url = "https://gitlab.apstudent.be/api/v4/groups"
    headers = {"PRIVATE-TOKEN": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Toon de groepen en hun ID's
    for groep in data:
        print(f"{groep.get('id')}: {groep.get('name')}")
    return data


def list_subgroups(group, token):
    # Functie om alle subgroepen van een specifieke groep op te lijsten
    url = f"https://gitlab.apstudent.be/api/v4/groups/{group}/subgroups"
    headers = {"PRIVATE-TOKEN": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Toon de subgroepen en hun ID's
    for groep in data:
        print(f"{groep.get('id')}: {groep.get('name')}")
    return data


def list_projects(group, token):
    # Functie om alle projecten in een groep op te lijsten
    url = f"https://gitlab.apstudent.be/api/v4/groups/{group}/projects"
    headers = {"PRIVATE-TOKEN": f"{token}"}
    response = requests.get(url, headers=headers)
    data = response.json()

    # Verzamel projectinformatie (naam en repository URL)
    project_info = [(project["name"], project['http_url_to_repo'])
                    for project in data]
    return project_info


def clone_projecten(project):
    # Functie om een Git-project te klonen naar de lokale machine
    url = project
    git.Repo.clone_from(url, os.getcwd() + "/imaplib-Python")


def process(group, token):
    # Functie om het hele proces uit te voeren: tonen, vragen om te klonen, en klonen
    projecten = list_projects(group, token)
    print("Dit zijn de projecten in de groep:")

    # Toon projecten en hun repository URL
    for naam, http in projecten:
        print(f"{naam}: {http}")

    # Vraag de gebruiker of ze de projecten willen klonen
    clone_input = input("Wil je de projecten klonen? (ja/nee): ").lower()
    if clone_input == 'ja':
        # Kloon de geselecteerde projecten
        for naam, http in projecten:
            clone_projecten(http)

    # Lijst alle subgroepen op en voer hetzelfde proces uit voor elke subgroep
    subgroepen = list_subgroups(group, token)
    for subgroup in subgroepen:
        process(subgroup['id'], token)


if __name__ == '__main__':
    # Controleer of het script correct wordt gebruikt
    if len(sys.argv) != 3:
        print("Gebruik: python script.py <studentennummer> <groepnaam>")
        sys.exit(1)

    # Haal studentennummer en groepsnaam op vanuit de command line argumenten
    studentennummer = sys.argv[1]
    group_name = sys.argv[2]

    # Vraag om de access token van de gebruiker
    token = input("Geef je access token: ")

    # Toon de beschikbare groepen ter referentie
    list_groepen(token)

    # Voer het hoofdproces uit met de opgegeven groep en token
    process(group_name, token)
