from requests.auth import HTTPBasicAuth
import requests


from payments import keys


def register_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    Api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(Api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_response = response.json()
    my_access_token = json_response["access_token"]

    return my_access_token
