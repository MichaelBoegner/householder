from fastapi import FastAPI
from app.api import meditate

app = FastAPI()

app.include_router(meditate.router)
