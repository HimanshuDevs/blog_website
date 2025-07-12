from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Form, File, UploadFile

# class CreateUserSchema(BaseModel):
#     username : str
#     role_id : int
#     email : str = Field(min_length=5, max_length=50)
#     password : Optional[str] = Field(min_length=5, max_length=20)
#     profile_pic : Optional[UploadFile] = File(None)


class CreateUserForm:
    def __init__(self,
        username    : str = Form(...),
        role_id     : int = Form(...),
        email       : Optional[str] = Form(..., min_length=5,max_length=50),
        password    : Optional[str] = Form(..., min_length=3, max_length=20),
        profile_pic : Optional[UploadFile] = File(None)
    ):
        self.username = username
        self.role_id = role_id
        self.email = email
        self.password = password
        self.profile_pic = profile_pic