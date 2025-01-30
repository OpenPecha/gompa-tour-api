from fastapi import APIRouter, HTTPException, Request

router = APIRouter()

@router.head("/", status_code=200)
async def check_translation(client_request: Request):
        return True
