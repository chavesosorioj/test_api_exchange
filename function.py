import requests


def get_authenticator():
    payload = {'username': 'Juucha', 'password': 'Anypointjucha1'}
    r = requests.post(' https://stgx.anypoint.mulesoft.com/accounts/login', data=payload)
    return r


def get_token():
    r = get_authenticator()
    data = r.json()
    return data.get("access_token")
