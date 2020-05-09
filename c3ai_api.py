import requests

# add countries
countries = ["Poland"]

# add metrics: ECDC_ConfirmedCases, ECDC_ConfirmedDeaths for example from ECDC (amongst others)
metrics = ["ECDC_ConfirmedCases"]

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
        "end": "2020-05-09"
    }
}


data_response = requests.post(resource, json=query, headers=headers)