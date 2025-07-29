from fastapi import APIRouter, Depends
from .schemas import CreateUserForm, UserLoginSchema
from .views import handle_create_user, handle_login
from config.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post('/create-user')
async def create_user(request: CreateUserForm = Depends(), db: AsyncSession = Depends(get_async_db)):
    return await handle_create_user(request,db)

@router.post('/login')
async def login(request:UserLoginSchema = Depends(), db:AsyncSession=Depends(get_async_db)):
    return await handle_login(request,db)
