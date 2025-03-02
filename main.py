from Apis.contollers import SwpcNoaaApi
from helpers.api_url import UrlEnums
from helpers.database import MySqlConnector
from helpers.mappers import PlanetaryKIndex


def main():

    db = MySqlConnector()
    print(db.get_by_id('planetary_kp_indices', 3))


main()
