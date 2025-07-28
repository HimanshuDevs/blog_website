from fastapi import APIRouter, Depends
from .schemas import CreateUserForm
from .views import handle_create_user
from config.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post('/create-user')
async def create_user(request: CreateUserForm = Depends(), db: AsyncSession = Depends(get_async_db)):
    return await handle_create_user(request,db)