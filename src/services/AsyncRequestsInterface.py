from abc import abstractmethod
from typing import Protocol, TypedDict


class Response(TypedDict):
    """Dicionario que representa a resposta da requisição."""

    url: str
    text: str
    status_code: int


class AsyncRequestsInterface(Protocol):
    """Interface para."""

    @abstractmethod
    async def get(self, url: str) -> Response: ...

    @abstractmethod
    async def close(self) -> None: ...
