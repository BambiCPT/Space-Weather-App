XRAY_FLARES: str = "goes/primary/xray-flares-7-day.json"
SOLAR_PROBABILITIES: str = "solar_probabilities.json"
PLANETARY_K: str = "planetary_k_index_1m.json"

def url (data_type: str):
    return f"https://services.swpc.noaa.gov/json/{data_type}"
