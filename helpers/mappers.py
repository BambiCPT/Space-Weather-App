import requests


class PlanetaryKIndex:
    def __init__(self, time_tag, kp_index, estimated_kp, kp):
        self.time_tag = time_tag
        self.kp_index = kp_index
        self.estimated_kp = estimated_kp
        self.kp = kp

    def __repr__(self):
        return f"PlanetaryKIndex(time_tag={self.time_tag}, kp_index={self.kp_index}, estimated_kp={self.estimated_kp}, kp={self.kp}\n)"


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


class XRayFlare:
    def __init__(self, begin_time, max_class_time, max_class, end_time):
        self.begin_time = begin_time
        self.end_time = end_time
        self.max_class_time = max_class_time
        self.max_class = max_class

    def __repr__(self):
        return f"XRayFlare(begin_time={self.begin_time}, end_time={self.end_time}, max_time={self.max_class_time}, max_class={self.max_class}\n)"


def xray_flare_mapper():
    try:
        response = requests.get(
            "https://services.swpc.noaa.gov/json/goes/primary/xray-flares-7-day.json", timeout=5)

        data = response.json()
        mapped_flares = []

        for i in data:
            flare_obj = XRayFlare(
                begin_time=i["begin_time"],
                end_time=i["end_time"],
                max_class_time=i["max_time"],
                max_class=i["max_class"],
            )
            mapped_flares.append(flare_obj)

        return mapped_flares

    except requests.exceptions.RequestException as e:
        return ("Request failed.", e)
