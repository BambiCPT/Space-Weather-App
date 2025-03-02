import requests

from helpers.api_url import Swpc, UrlEnums


class SwpcNoaaApi():
    def _get(self, url_param: UrlEnums) -> str | bool:
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
