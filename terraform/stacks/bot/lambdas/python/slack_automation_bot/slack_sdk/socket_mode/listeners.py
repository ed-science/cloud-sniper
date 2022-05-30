from typing import Optional

from slack_sdk.socket_mode.request import SocketModeRequest


class WebSocketMessageListener:
    def __call__(self, message: dict, raw_message: Optional[str] = None):  # noqa: F821
        raise NotImplementedError()


class SocketModeRequestListener:
    def __call__(self, request: SocketModeRequest):  # noqa: F821
        raise NotImplementedError()
