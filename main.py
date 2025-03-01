from Apis.contollers import SwpcNoaaApi
from helpers.api_url import UrlEnums


def main():
    data_and_handled = SwpcNoaaApi()._get(UrlEnums.SOLAR_PROBABILITIES)
    print(data_and_handled)


main()
