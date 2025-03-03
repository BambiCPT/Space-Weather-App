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

    # to test delete_by_id()
    # print(db.delete_by_id('planetary_kp_indices', 2))

    # to test get_all()
    # print(db.get_all('planetary_kp_indices'))

    # tests get_by_id() and also prints the before updated values
    print(db.get_by_id('planetary_kp_indices', 5))
    # updates values using mock_data object
    db.update_by_id("planetary_kp_indices", 5, mock_data)
    # shows the updated values vs the original values
    print(db.get_by_id('planetary_kp_indices', 5))


main()
