from Apis.contollers import SwpcNoaaApi
from helpers.api_url import UrlEnums
from helpers.database import MySqlConnector
from helpers.mappers import PlanetaryKIndex


def main():

    db = MySqlConnector()

    mock_data = PlanetaryKIndex(
        kp="0Z",
        estimated_kp=4,
        time="2025-03-01 17:58:00",
    )

    print(db.get_by_id('planetary_kp_indices', 5))
    db.update_by_id("planetary_kp_indices", 5, mock_data)
    print(db.get_by_id('planetary_kp_indices', 5))


main()
