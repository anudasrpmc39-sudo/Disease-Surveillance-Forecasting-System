import requests
from config import DHIS2_BASE_URL, USERNAME, PASSWORD

def fetch_data():
    url = f"{DHIS2_BASE_URL}/analytics.json"
    
    params = {
        "dx": "Measles_cases;Dengue_cases;Diarrhea_cases",
        "pe": "LAST_30_DAYS",
        "ou": "LEVEL-4"
    }

    response = requests.get(url, params=params, auth=(USERNAME, PASSWORD))
    data = response.json()

    return data
