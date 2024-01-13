import requests


def getGroepId():
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}

    groepNaam = "PythonAdvancedOscarAlexander"
    url = "https://gitlab.apstudent.be/api/v4/groups"

    params = {"search": groepNaam}
    res = requests.get(url, headers=headers, params=params)

    groepId = 0

    if res.status_code == 200:
        groepen = res.json()
        for groep in groepen:
            if groep.get('name') == groepNaam:
                groepId = groep.get('id')
    return groepId


def maakSubgroep(groepId):
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}
    name = "test2"
    parentId = str(groepId)  # voor subgrpep moet je een parent id meegeven
    url1 = "https://gitlab.apstudent.be/api/v4/groups"
    data = {"name": name, "path": name, "parent_id": parentId}

    res = requests.post(url1, headers=headers, data=data)

    if res.status_code == 201:  # toon bericht op scherm
        subGroepInfo = res.json()
        print("Subgroep succesvol aangemaakt:")
        print(f"Subgroep ID: {subGroepInfo.get('id')}")
        print(f"Subgroep naam: {subGroepInfo.get('name')}")
        print(f"Pad: {subGroepInfo.get('path')}")
    else:
        print(
            f"Er is een fout opgetreden")


maakSubgroep(getGroepId())
