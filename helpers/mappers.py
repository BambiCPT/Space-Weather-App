import requests


class PlanetaryKIndex:
    def __init__(self, time_tag, kp_index, estimated_kp, kp):
        self.time_tag = time_tag
        self.kp_index = kp_index
        self.estimated_kp = estimated_kp
        self.kp = kp

    def __repr__(self):
        return f"PlanetaryKIndex(time_tag={self.time_tag}, kp_index={self.kp_index}, estimated_kp={self.estimated_kp}, kp={self.kp})"


def kpi_index_mapper():
    try:
        response = requests.get(
            "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json", timeout=5)

        data = response.json()
        mapped_pki = []

        for i in data:
            pki_obj = PlanetaryKIndex(**i)
            mapped_pki.append(pki_obj)

        return mapped_pki

    except requests.exceptions.RequestException as e:
        return ("Request failed.", e)
