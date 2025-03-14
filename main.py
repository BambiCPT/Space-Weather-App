from Apis.contollers import SwpcNoaaApi


def main():
    test = SwpcNoaaApi()._solar_flares_get_all()
    print(test)


main()
