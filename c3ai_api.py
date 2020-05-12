import requests
import ujson

from covid19 import get_covid_country_data

# add countries
countries = [location for location in open("data/locations.csv", "r").readlines()]
countries = ['Poland']

# add metrics: ECDC_ConfirmedCases, ECDC_ConfirmedDeaths for example from ECDC (amongst others)
metrics = ["ECDC_ConfirmedCases"]#, "ECDC_ConfirmedDeaths", "NYT_ConfirmedCases", "NYT_ConfirmedDeaths"]

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

get_covid_country_data(resource, 'Poland', query)