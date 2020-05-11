import requests
import ujson

# add countries
countries = [location for location in open("data/locations.csv", "r").readlines()]
countries = ['Poland']

# add metrics: ECDC_ConfirmedCases, ECDC_ConfirmedDeaths for example from ECDC (amongst others)
metrics = ["ECDC_ConfirmedCases", "ECDC_ConfirmedDeaths"]

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

resource = "https://api.c3.ai/covid/api/1/outbreaklocation/evalmetrics"

query = {
    "spec": {
        "ids": countries,
        "expressions": metrics,
        "interval": "DAY",
        "start": "2020-01-01",
        "end": "2020-05-11"
    }
}
query = dict(query)
data_response = requests.post(resource, json=query, headers=headers)

if data_response.status_code == 200:
    f = open(f"data/{countries[0]}.json", "w")
    f.writelines(data_response.json())
    f.close()
