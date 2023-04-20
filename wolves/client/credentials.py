from wolves.client.rest.auth import get_bearer


class Credentials:
    def __init__(self):
        self._refresh_token = None

    @property
    def refresh_token(self):
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value):
        self._refresh_token = value

    @property
    def bearer(self):
        return get_bearer(self._refresh_token)
