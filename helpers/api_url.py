from enum import Enum


class UrlEnums(Enum):
    XRAY_FLARES: str = "goes/primary/xray-flares-7-day.json"
    SOLAR_PROBABILITIES: str = "solar_probabilities.json"
    PLANETARY_K: str = "planetary_k_index_1m.json"


class Swpc():
    @staticmethod
    def get_url(data_type: UrlEnums) -> str:
        return f"https://services.swpc.noaa.gov/json/{data_type.value}"
