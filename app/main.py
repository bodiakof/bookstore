import logging

# Importing logging_config sets up logging handlers and format globally
from app.core import logging_config 

from fastapi import FastAPI

from app.api import book


app = FastAPI()

app.include_router(book.router, prefix='/books', tags=['Books'])

logger = logging.getLogger(__name__)
logger.info("FastAPI app started")
