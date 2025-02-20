from httpx import AsyncClient
from typing import AsyncGenerator

# Common dependencies for the gateway. For example, an asynchronous HTTP client is provided as a dependency.
# Using a factory function (Factory Pattern) here to create a client.
async def get_http_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient() as client:
        yield client
