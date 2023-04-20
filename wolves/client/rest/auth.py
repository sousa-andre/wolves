import requests

from wolves.client.rest.constants import AUTH_REST_URL
from wolves.client.rest.exceptions import AuthenticationFailed


def get_bearer(refresh_token: str):
    req = requests.post(f'{AUTH_REST_URL}/players/createIdToken', json={
        'refreshToken': refresh_token,
    })
    data = req.json()
    try:
        return data['idToken']
    except KeyError:
        raise AuthenticationFailed()
