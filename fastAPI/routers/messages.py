from fastapi import APIRouter

router = APIRouter()

@router.get("/public/")
async def get_public():
    return { "message": "The API doesn't require an access token to share this message."}


@router.get("/protected")
async def get_protected():
    return {"message": "The API successfully recognized you as an admin."}


@router.get("/admin")
async def get_admin():
    return {"message": "Hello World"}