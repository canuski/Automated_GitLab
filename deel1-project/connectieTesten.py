import requests
token = input("Geef je Gitlab access token: ")
url = "https://gitlab.com/api/v4/user"  # endpoint voor user info
headers = {f"PRIVATE-TOKEN": token}  # header met token voor auth
res = requests.get(url, headers=headers)
if res.status_code == 200:
    userInfo = res.json()
    print("User info:")
    print(f"Username: {userInfo['username']}")
    print(f"Name: {userInfo['name']}")
    print(f"Email: {userInfo['email']}")
else:
    print(res.status_code)
