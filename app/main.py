from fastapi import FastAPI
from app.api import book


app = FastAPI()

app.include_router(book.router, prefix='/books', tags=['Books'])
