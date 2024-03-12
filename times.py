import requests
import json
import re

def get_times():
    response = requests.get("https://mawaqit.net/fr/mosquee-goussainville")
    if (response.status_code == 200):
        times = re.search(r'"times":(\[.+?\]),', response.text).group(1)
        times = json.loads(times)
        print(times)
        return times
    return None
