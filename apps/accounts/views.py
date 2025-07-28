from fastapi import UploadFile, HTTPException
from pathlib import Path
import shutil
from .models import AuthUsers
from sqlalchemy.ext.asyncio import AsyncSession
from config.settings import MEDIA_USERS_DIR
from utils.file_validator import validate_image_upload


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
        password     = request.password,
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