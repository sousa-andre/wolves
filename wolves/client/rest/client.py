import requests
from aiohttp import ClientSession

from wolves.client.credentials import Credentials
from wolves.client.rest.constants import SOCKETIO_WSS_URL, REST_URL


class WolvesRestClient:
    def __init__(self, *, credentials: Credentials):
        self._credentials = credentials
        self._session = ClientSession()

    def get_client_core(self, uri):
        return self._session.get(f'{REST_URL}{uri}', headers={
            'Authorization': f'Bearer {self._credentials.bearer}'
        })

    async def close(self):
        await self._session.close()