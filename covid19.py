import logging
import requests
import ujson

from utils.timer import Timer


log_file = "./log/api_log.log"

api_header = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

def get_covid_country_data(resource, country, query, source, header=None):
    t = Timer()
    logging.basicConfig(level=logging.INFO, 
                                 filename=log_file, 
                                 format="%(asctime)s: %(process)d - %(levelname)s - %(message)s",
                                 datefmt="%d-%b-%yy %H:%M:%S")
    header = header or api_header

    t.start()
    result = requests.post(resource, json=query, headers=header)
    api_read_elapsed = t.stop()

    if result.status_code != 200:
        logging.error(f"API call for query {query} for endpoint {resource} failed, please re-run")
        return result
    
    try:
        filenm = f"./data/{country}-{source}.json"
        t.start()
        f = open(filenm, "w")
        f.writelines(ujson.dumps(result.json()))
        f.close()
        write_elapsed = t.stop()
        logging.info(f"Written {filenm} successfully, api-read-time {api_read_elapsed:0.4f}, json-write-time {write_elapsed:0.4f}")
        return result
    except Exception as e:
        logging.error(f"Unable to write {filenm} - {e}")

