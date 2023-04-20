import json

from socketio import AsyncClient

from wolves.client.credentials import Credentials


class SocketIOConnector(AsyncClient):
    def __init__(self, update_callback, *, credentials: Credentials, debug=False, **kwargs, ):
        super().__init__(engineio_logger=debug, logger=debug, **kwargs)

        self._credentials = credentials

        self._update_callback = update_callback
        self.on('*', self.on_any)

    async def on_any(self, data, event_type=None):
        if event_type is not None:
            event_type = json.loads(event_type)
        await self._update_callback(data, event_type)

    def connect_directly_observe(self):
        return self.connect(
            f'https://api-game.wolvesville.com/socket.io/?firebaseToken={self._credentials.bearer}&gameMode=en&spectate=true&randomAvatarSlot=false&ids=1',
            transports=['websocket'])
