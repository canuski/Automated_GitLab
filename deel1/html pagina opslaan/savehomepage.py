import requests
r = requests.get('https://www.ap.be/')
data = r.text
with open("homepage.html", "w") as html_file:
    html_file.write(data)
