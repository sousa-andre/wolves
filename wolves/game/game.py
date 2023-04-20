import asyncio
from asyncio import Queue

from wolves.client.credentials import Credentials
from wolves.client.rest.client import WolvesRestClient
from wolves.factory.game.event_factory import EventFactory

from wolves.client.sio.socketio_connector import SocketIOConnector
from wolves.store.in_memory import InMemoryAsyncStore


class ObservableGame:
    def __init__(self, *, http_client=None, sio_connector=None, store=None):
        self._credentials = Credentials()
        self._store = store or InMemoryAsyncStore()
        self._http_client = http_client or WolvesRestClient(credentials=self._credentials)
        self._socket = sio_connector or SocketIOConnector(self._new_sio_event,
                                                          credentials=self._credentials)

    @property
    def http(self):
        return self._http_client

    def login(self, refresh_token: str):
        self._credentials.refresh_token = refresh_token

    async def _new_sio_event(self, event_type, data):
        await self._store.put(EventFactory.create(event_type).from_json(data, event_type))

    async def spectate(self):
        await self._socket.connect_directly_observe()

    async def next_event(self):
        while True:
            yield await self._store.get()

    async def cleanup(self):
        await asyncio.gather(self._http_client.close())
