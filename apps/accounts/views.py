from fastapi import UploadFile, HTTPException
from pathlib import Path
import shutil

MEDIA_DIR = Path("media/users")
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

async def handle_create_user(request):
    # Validate file type
    if request.profile_pic:
        if not request.profile_pic.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Only image files are allowed.")

        # Save profile picture
        filename = f"{request.profile_pic.filename}"
        file_path = MEDIA_DIR / filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(request.profile_pic.file, buffer)

        profile_pic_path = str(file_path)
    else:
        profile_pic_path = None

    # Simulate DB save (replace this with real DB interaction)
    user_data = {
        "username": request.username,
        "role_id": request.role_id,
        "email": request.email,
        "password": request.password,
        "profile_pic": profile_pic_path
    }

    return {
        "status": "success",
        "message": "User created successfully",
        "user": user_data
    }