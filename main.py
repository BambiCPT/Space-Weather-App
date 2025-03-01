from Apis.contollers import SwpcNoaaApi
from helpers.api_url import UrlEnums
from helpers.database import MySqlConnector
from helpers.mappers import PlanetaryKIndex


def main():
    data_and_handled = SwpcNoaaApi()._get(UrlEnums.PLANETARY_K)

    kpi_index_mapper = PlanetaryKIndex(  # <- initialized class object
        kp=None,
        estimated_kp=None,
        time=None
    )

    # issue is that because mappers are class methods, they need to be called on an initialized class object...
    data = kpi_index_mapper.kpi_index_mapper(data_and_handled)
    connector = MySqlConnector()

    print(connector.insert_data("planetary_kp_indices", data))


main()
