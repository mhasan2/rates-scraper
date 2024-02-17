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


# Selenium required for ace
# url = "https://acemoneytransfer.com/Bangladesh/Send-Money-to-Bangladesh"

def ria_auth_token():
    url = "https://public.riamoneytransfer.com/Authorization/session"
    headers = {"accept": "application/json, text/plain, */*",
               "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
               }
    page = requests.get(url, headers=headers)
    return page.json()["authToken"]["jwtToken"]

url = "https://public.riamoneytransfer.com/MoneyTransferCalculator/Calculate"
headers = {"accept": "application/json, text/plain, */*",
           "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
           "apptype": "2",
           "appversion": "4.0",
           "authorization": "Bearer {}".format(ria_auth_token()),
           "client-type": "App",
           "content-type": "application/json",
           "culturecode": "en-GB",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
           }

# data = {
#     "selections": {"countryTo": "BD", "amountFrom": 100, "amountTo": None, "currencyFrom": "USD", "currencyTo": None,
#                    "paymentMethod": "DebitCard", "deliveryMethod": "BankDeposit", "shouldCalcAmountFrom": False,
#                    "shouldCalcVariableRates": True, "state": None, "agentToId": None, "stateTo": None,
#                    "agentToLocationId": None, "promoCode": None, "promoId": 0, "transferReason": None,
#                    "countryFrom": "GB"}}
data = {
    "selections": {"countryTo": "BD", "amountFrom": 100, "amountTo": None, "currencyFrom": "USD", "currencyTo": None,
                   "paymentMethod": "DebitCard", "deliveryMethod": "BankDeposit", "shouldCalcAmountFrom": False,
                   "shouldCalcVariableRates": True, "state": None, "agentToId": None, "stateTo": None,
                   "agentToLocationId": None, "promoCode": None, "promoId": 0, "transferReason": None,
                   "countryFrom": "GB"}}

page = requests.post(url, data=data, headers=headers)

print(page.text)
# page_json = page.json()
# print(json.dumps(page_json, indent=2))
