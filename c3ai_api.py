import requests
import sys
import ujson

from covid19 import get_covid_country_data

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

# mandatory header for api
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# main api resource
resource = "https://api.c3.ai/covid/api/1/outbreaklocation/evalmetrics"

def main(countries) -> None:
    for country in countries:
        for metric in metrics:

            query = {
                "spec": {
                    "ids": [country],
                    "expressions": [metric],
                    "interval": "DAY",
                    "start": "2020-01-01",
                    "end": "2020-06-10"
                }
            }
            res = get_covid_country_data(resource, country, query, metric)
            print(f"country data: {country} status: {res.status_code}")

if __name__ == '__main__':
    # get country loc list
    countries = [location.rstrip('\n') for location in open("data/locations.csv", "r").readlines()]
    
    if len(sys.argv) > 1:
        for cli_country in sys.argv[1:]:
            if cli_country not in countries:
                raise ValueError(f"Country '{cli_country}' not valid location for api metric")
        main(sys.argv[1:])
    else:
        print("Enter specific country (comma separated)")
        cli_countries = list(input().split(','))
        cli_countries = cli_countries or countries
        main(countries=cli_countries)
