from typing import override

from httpx import AsyncClient

from services.interfaces.AsyncRequestsInterface import (
    AsyncRequestsInterface,
    Response,
)


class HttpxAdapter(AsyncRequestsInterface):
    """Adapter de um cliente Asyncrono do HTTPX."""

    def __init__(self, headers: dict, timeout: float = 10.0) -> None:
        self.__client: AsyncClient = AsyncClient(
            headers=headers,
            timeout=timeout,
        )

    @override
    async def get(self, url: str) -> Response:
        """Faz uma requisição GET para a url passada."""
        response = await self.__client.get(url)
        return {
            "url": str(response.url),
            "status_code": response.status_code,
            "text": response.text,
        }

    @override
    async def aclose(self) -> None:
        """Fecha o cliente asyncrono do httpx."""
        await self.__client.aclose()
