import logging
import requests
import ujson


log_file = "./log/api_log.log"

api_header = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

def get_covid_country_data(resource, country, query, header=None):
    logging.basicConfig(level=logging.INFO, 
                                 filename=log_file, 
                                 format="%(asctime)s: %(process)d - %(levelname)s - %(message)s",
                                 datefmt="%d-%b-%yy %H:%M:%S")
    header = header or api_header
    result = requests.post(resource, json=query, headers=header)

    if result.status_code != 200:
        logging.error(f"API call for query {query} for endpoint {resource} failed, please re-run")
        return
    
    try:
        filenm = f"./data/{country}.json"
        f = open(filenm, "w")
        f.writelines(ujson.dumps(result.json()))
        f.close()
        logging.info(f"Written {filenm} successfully")
    except Exception as e:
        logging.error(f"Unable to write {filenm} - {e}")

