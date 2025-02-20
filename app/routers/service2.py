from fastapi import APIRouter, Depends, HTTPException
import httpx
from app.config import settings
from app.dependencies import get_http_client

router = APIRouter()

@router.get("/data", summary="Get Data from Service 2")
async def get_data(client: httpx.AsyncClient = Depends(get_http_client)):
    try:
        response = await client.get(f"{settings.SERVICE2_URL}/data")
        response.raise_for_status()
    except httpx.ConnectError as e:
        raise HTTPException(status_code=503, detail="Service 2 is unavailable: " + str(e))
    return response.json()
