import unittest

import respx
from httpx import Response as HttpxResponse

from src.services.HttpxAdapter import HttpxAdapter


class TestHttpxAdapter(unittest.IsolatedAsyncioTestCase):
    @respx.mock
    async def test_metdo_get(self):
        sei_la = HttpxAdapter(
            headers={
                "User-Agent": (
                    "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0',"
                ),
            },
        )

        respx.get("https://www.google.com/").mock(
            return_value=HttpxResponse(
                200,
                text="Olá",
            ),
        )

        response = await sei_la.get("https://www.google.com/")

        assert isinstance(response, dict)
        assert response["text"] == "Olá"
        assert response["status_code"] == 200
        assert response["url"] == "https://www.google.com/"
