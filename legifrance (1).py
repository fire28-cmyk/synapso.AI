
import os
import requests

def get_token():
    client_id = os.getenv("PISTE_CLIENT_ID")
    client_secret = os.getenv("PISTE_CLIENT_SECRET")
    url = "https://sandbox-oauth.piste.gouv.fr/api/oauth/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "openid"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        return None
