import requests

token = input("Geef je Gitlab access token: ")
groepNaam = "PythonAdvancedOscarAlexandertest4"
url = "https://gitlab.apstudent.be/api/v4/groups"
headers = {"PRIVATE-TOKEN": token}
data = {
    "name": groepNaam,
    "path": groepNaam
}

print("Request data:", data)
res = requests.post(url, headers=headers, json=data)

print("Response content:", res.content)
print("Status code:", res.status_code)

if res.status_code == 201:
    groep_info = res.json()
    print("Groep succesvol aangemaakt:")
    print(f"Groep ID: {groep_info.get('id')}")
    print(f"Groepnaam: {groep_info.get('name')}")
    print(f"Pad: {groep_info.get('path')}")
else:
    print("Er is een fout opgetreden bij het aanmaken van de groep.")
