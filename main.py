from fastapi import FastAPI
from apps.accounts import router as accounts_router
from apps.blogs import router as blogs_router
from apps.api import router as api_router


app = FastAPI()