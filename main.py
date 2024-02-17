import requests

URL = "https://www.taptapsend.com/"
page = requests.get(URL)

print(page.text)
