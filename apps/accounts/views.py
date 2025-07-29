from fastapi import UploadFile, HTTPException, status
from pathlib import Path
import shutil
from .models import AuthUsers
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import MEDIA_USERS_DIR
from utils.file_validator import validate_image_upload
from utils.hashing import hash_password, verify_password
from utils.jwt_token import create_access_token
from sqlalchemy.future import select


async def handle_create_user(request, db):
    if request.profile_pic:
        await validate_image_upload(request.profile_pic)

        filename = f"{request.profile_pic.filename}"
        file_path = MEDIA_USERS_DIR / filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(request.profile_pic.file, buffer)

        profile_pic_path = str(file_path)
    else:
        profile_pic_path = None

    user_data = AuthUsers(
        username     = request.username,
        role_id      = request.role_id,
        email        = request.email,
        password     = hash_password(request.password),
        profile_pic  = profile_pic_path
    )
    db.add(user_data)
    await db.commit()
    await db.refresh(user_data)

    return {
        "status": "success",
        "message": "User created successfully",
        "user": user_data
    }

async def handle_login(request, db):

    users_obj = select(AuthUsers).filter(AuthUsers.email == request.username)
    result = await db.execute(users_obj)
    user_obj = result.scalars().first()

    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details='invalid credentials')
    
    if not verify_password(request.password, user_obj.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details='Invalid password')
    user_data = {'user_id':user_obj.id, 'user_email':user_obj.email}
    access_token = create_access_token(user_data)
    return {"message":"Login successfully", "access_token":access_token}