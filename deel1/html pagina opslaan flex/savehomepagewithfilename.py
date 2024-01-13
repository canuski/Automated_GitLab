import requests
import sys
r = requests.get('https://www.ap.be/')

fileName = sys.argv[1]
data = r.text
with open(f"{fileName}", "w") as html_file:
    html_file.write(data)
