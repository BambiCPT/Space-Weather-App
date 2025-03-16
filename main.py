from Apis.contollers import SwpcNoaaApi


def main():
    test = SwpcNoaaApi()._planetary_get_by_id(1)
    print(test)


main()
