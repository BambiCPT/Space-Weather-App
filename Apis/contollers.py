import requests

from helpers.api_url import Swpc, UrlEnums
from helpers.database import MySqlConnector, TableEnum
from helpers.mappers import Mappers


class SwpcNoaaApi():
    @staticmethod
    def __get(url_param: UrlEnums) -> str | bool:
        url = Swpc.get_url(url_param)
        data = SwpcNoaaApi.__handle_call(url)
        return data

    @staticmethod
    def __handle_call(url: str) -> requests.Response | bool:
        try:
            req = requests.get(url, timeout=10)
            if req.status_code != 200 or req.headers['content-type'] != 'application/json':
                print(f"Something went wrong while calling: {url}")
                return False
            if not req.json():
                print("Error: Empty response")
                return False
            return req.json()

        except Exception as e:
            print(f"Call error: {e}")
            return False

    def _fetch_planetary_kp(self):
        data = self.__get(UrlEnums.PLANETARY_K)
        MySqlConnector().insert_data(TableEnum.PLANETARY_KP, Mappers().planetary_kp(data))

    def _fetch_solar_flares(self):
        data = self.__get(UrlEnums.XRAY_FLARES)
        MySqlConnector().insert_data(TableEnum.SOLAR_FLARE, Mappers().xray_flare(data))

    def _fetch_solar_flares_probability(self):
        data = self.__get(UrlEnums.SOLAR_PROBABILITIES)
        MySqlConnector().insert_data(
            TableEnum.SOLAR_FLARE_PROBABILITY, Mappers().solar_proability(data))
