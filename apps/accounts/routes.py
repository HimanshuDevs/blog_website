from fastapi import APIRouter, Depends
from .schemas import CreateUserForm
from .views import handle_create_user

router = APIRouter()


@router.post('/create-user')
async def create_user(request: CreateUserForm = Depends()):
    return await handle_create_user(request)