import requests
import csv

entered_groepNaam = None


def getGroepNaam():
    global entered_groepNaam
    if entered_groepNaam:
        return entered_groepNaam
    else:
        gnaam = input(
            "Geef de groepsnaam voor wie je de ID wil hebben: ").strip()
        entered_groepNaam = gnaam
        return gnaam


def getGroepId():
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}

    groepNaam = getGroepNaam()
    url = "https://gitlab.apstudent.be/api/v4/groups"

    params = {"search": groepNaam}
    res = requests.get(url, headers=headers, params=params)

    groepId = 0

    if res.status_code == 200:
        groepen = res.json()
        for groep in groepen:
            if groep.get('name') == groepNaam:
                groepId = groep.get('id')

    else:
        print(f"{res.status_code}")
    print(groepId)
    return groepId


def getGroepIdVak(vakNaam):
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}
    groep_name = entered_groepNaam
    subgroup_name = vakNaam
    groep_url = f"https://gitlab.apstudent.be/api/v4/groups/{groep_name}"
    res = requests.get(groep_url, headers=headers)

    groepId = 0

    if res.status_code == 200:
        groep_data = res.json()

        subgroeps_url = f"https://gitlab.apstudent.be/api/v4/groups/{groep_data['id']}/subgroups"
        subgroeps_res = requests.get(subgroeps_url, headers=headers)

        if subgroeps_res.status_code == 200:
            subgroeps_data = subgroeps_res.json()

            for subgroep in subgroeps_data:
                if subgroep['name'] == subgroup_name:
                    groepId = subgroep['id']
                    break

    else:
        print(f"Error: {res.status_code}")
    return groepId


def getIdGroep(vakNaam, groepNaam):
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}
    vakId = getGroepIdVak(vakNaam)
    subgroup_name = groepNaam
    groep_url = f"https://gitlab.apstudent.be/api/v4/groups/{vakId}"
    res = requests.get(groep_url, headers=headers)

    groepId = 0

    if res.status_code == 200:
        groep_data = res.json()

        subgroeps_url = f"https://gitlab.apstudent.be/api/v4/groups/{groep_data['id']}/subgroups"
        subgroeps_res = requests.get(subgroeps_url, headers=headers)

        if subgroeps_res.status_code == 200:
            subgroeps_data = subgroeps_res.json()

            for subgroep in subgroeps_data:
                if subgroep['name'] == subgroup_name:
                    groepId = subgroep['id']
                    break

    else:
        print(f"Error: {res.status_code}")
    return groepId


def listId(type, vakNaam=None, groepsNaam=None):
    if type == 'vak':
        return getGroepId()
    elif type == 'groep':
        return getGroepIdVak(vakNaam)
    elif type == 'student':
        return getIdGroep(vakNaam, groepsNaam)
    else:
        return 'error'


def maakSubgroep(groepId, Name):
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}
    name = Name
    parentId = str(groepId)
    url1 = "https://gitlab.apstudent.be/api/v4/groups"

    data = {"name": name, "path": name, "parent_id": parentId}
    res = requests.post(url1, headers=headers, data=data)

    if res.status_code == 201:
        subGroepInfo = res.json()
        print("Subgroep succesvol aangemaakt:")
        print(f"Subgroep ID: {subGroepInfo.get('id')}")
        print(f"Subgroep naam: {subGroepInfo.get('name')}")
        print(f"Pad: {subGroepInfo.get('path')}")

    else:
        print(f"Er is een fout opgetreden")


csvFile = "testFile.csv"  # pad naar csv file
with open(csvFile, newline='') as csvfile:  # csv file openen
    reader = csv.reader(csvfile)  # csv reader doen
    found_vakken = {}
    found_groepen = {}
    found_studenten = {}  # dicts voor storage
    next(reader, None)  # over de header rij gaan

    for row in reader:
        vak, groep, studentEmail = row
        vakNaam = str(vak)
        groepNaam = str(groep)
        studentenMail = str(studentEmail)

        key_vak_groep = f"{vakNaam}_{groepNaam}"

        if vakNaam not in found_vakken:
            id = listId('vak')
            maakSubgroep(id, vakNaam)
            found_vakken.update({vakNaam: 'Bestaat'})

        if key_vak_groep not in found_groepen:
            idG = listId('groep', vakNaam)
            maakSubgroep(idG, groepNaam)
            found_groepen.update({key_vak_groep: 'Bestaat'})

        idS = listId('student', vakNaam, groepNaam)
        maakSubgroep(idS, studentenMail)

    print(found_vakken)
    print(found_groepen)
