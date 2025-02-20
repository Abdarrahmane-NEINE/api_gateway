from fastapi import APIRouter, Header, HTTPException, status
from app.schemas import Token

router = APIRouter()


@router.post("/verify", response_model=Token, summary="Simulated Token Verification")
async def verify_authentication_token():
    """
    Simulates verification by returning a fixed token response, ignoring the actual header content.
    """
    # Always return the same token
    return {"access_token": "simulated-token", "token_type": "bearer"}