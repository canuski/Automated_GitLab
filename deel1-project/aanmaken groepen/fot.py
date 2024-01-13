import requests


def getGroepIdSub(vakNaam):
    token = "glpat-pzeeaf6QQxZyoRyeJwEz"
    headers = {"PRIVATE-TOKEN": token}
    groep_name = 'test54'
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
    vakId = getGroepIdSub(vakNaam)
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
        pass
    elif type == 'groep':
        pass
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


Sid = getIdGroep('programmeren1', 'groep1')

maakSubgroep(Sid, 'oscaralexander')
