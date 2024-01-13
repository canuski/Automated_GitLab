import getpass
username = input("Geef je username in: ")
password = getpass.getpass("Geef je wachtwoord in: ")

print("Je hebt gekozen:")
print(f"Username: {username}")
print(f"Passowrd: {password}")
