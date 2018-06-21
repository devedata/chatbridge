import requests


def main():
    r = requests.post(
        URL,
        params={
            "authtoken": AUTH_TOKEN,
            "zc_ownername": ZC_OWNERNAME,
            "scope": SCOPE,
            "raw": RAW
        },
        # headers={
        #     'Content-type': 'application/json',
        #     'Authorization': 'Zoho-authtoken ' + AUTH_TOKEN
        # },
    )
    print(r.status_code, r.reason)


if __name__ == '__main__':
    URL = 'https://creator.zoho.eu/api/json/pizza-order-app/view/Pizza_Order_Report'
    AUTH_TOKEN = 'a4bfe31a5af25dbcf6a77d3bd1d0a3b9'
    SCOPE = 'creatorapi'
    ZC_OWNERNAME = 'serg.syuzev'
    RAW = 'true'

    main()
