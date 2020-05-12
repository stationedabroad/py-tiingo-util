import requests
import ujson

from covid19 import get_covid_country_data

# add countries
countries = [location for location in open("data/locations.csv", "r").readlines()]
countries = ['Poland']

# add metrics: ECDC_ConfirmedCases, ECDC_ConfirmedDeaths for example from ECDC (amongst others)
metrics = ["ECDC_ConfirmedCases", 
           "ECDC_ConfirmedDeaths", 
           "NYT_ConfirmedCases", 
           "NYT_ConfirmedDeaths",
           "JHU_ConfirmedCases", 
           "JHU_ConfirmedDeaths", 
           "JHU_ConfirmedRecoveries", 
           "JHU_ConfirmedCasesInterpolated",
           "CovidTrackingProject_ConfirmedCases", 
           "CovidTrackingProject_ConfirmedDeaths", 
           "CovidTrackingProject_ConfirmedHospitalizations",
           "CovidTrackingProject_NegativeTests", 
           "CovidTrackingProject_PendingTests",
           "WHO_ConfirmedCases", 
           "WHO_ConfirmedDeaths",
           ]

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

resource = "https://api.c3.ai/covid/api/1/outbreaklocation/evalmetrics"

for metric in metrics:

    query = {
        "spec": {
            "ids": countries,
            "expressions": [metric],
            "interval": "DAY",
            "start": "2020-01-01",
            "end": "2020-05-11"
        }
    }

    res = get_covid_country_data(resource, 'Poland', query, metric)