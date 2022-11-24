from typing import *
from fastapi import FastAPI
from pydantic import *
from config import engine
import router

from model.db import step_db_model
from model.db import process_db_model

step_db_model.Base.metadata.create_all(bind=engine)
process_db_model.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router.router, prefix="/process", tags=["process"])

