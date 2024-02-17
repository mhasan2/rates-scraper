import requests
import json
from pprint import pprint


def tap_tap_bdt():
    url = "https://api.taptapsend.com/api/fxRates"
    headers = {
        "appian-version": "web/2022-05-03.0",
        "x-device-id": "web",
        "x-device-model": "web"
    }
    page = requests.get(url, headers=headers)

    page_json = page.json()

    for country in page_json["availableCountries"]:
        if country["currency"] == "GBP":
            for corridor in country["corridors"]:
                if corridor["currency"] == "BDT":
                    return corridor["fxRate"]

# print(json.dumps(page_json, indent=2))
