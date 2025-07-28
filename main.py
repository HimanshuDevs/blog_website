from fastapi import FastAPI
from apps.accounts.routes import router as accounts_router
from apps.blogs.routes import router as blogs_router
from apps.api.routes import router as api_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(accounts_router, prefix='/accounts',tags=['User'])
app.include_router(blogs_router, prefix='/blogs', tags=['Blogs'])
app.include_router(api_router, prefix='/api', tags=['API'])

# to fetch the media files
app.mount("/media", StaticFiles(directory="media"), name="media")