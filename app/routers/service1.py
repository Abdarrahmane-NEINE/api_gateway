from fastapi import APIRouter, Depends, HTTPException
import httpx
from app.config import settings
from app.dependencies import get_http_client

router = APIRouter()

# Uses dependency injection for HTTP client and centralized configuration.
@router.get("/items", summary="Get Items from Service 1")
async def get_items(client: httpx.AsyncClient = Depends(get_http_client)):
    try:
        # Demonstrates the Facade pattern to hide the details of external service calls.
        # Proxy call to Service 1
        response = await client.get(f"{settings.SERVICE1_URL}/items")
        response.raise_for_status()
    except httpx.ConnectError as e:
        raise HTTPException(status_code=503, detail="Service 1 is unavailable: " + str(e))
    return response.json()
