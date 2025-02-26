xray_flares = "goes/primary/xray-flares-7-day.json"
solar_probabilities = "solar_probabilities.json"
planetary_k = "planetary_k_index_1m.json"
api_handles = [xray_flares, solar_probabilities, planetary_k]

def url (data_type):
    return f"https://services.swpc.noaa.gov/json/{data_type}"
