from abc import abstractmethod
from typing import Protocol, TypedDict, final


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
    async def aclose(self) -> None: ...

    @final
    async def __aenter__(self) -> "AsyncRequestsInterface":
        """Retorna uma AsyncRequestsInterface quando usado async with."""
        return self

    @final
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: object,
    ) -> None:
        """Fecha o AsyncRequestsInterface quando sair do bloco async with."""
        await self.aclose()
