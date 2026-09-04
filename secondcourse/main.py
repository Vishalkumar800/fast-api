from secondcourse.app.routes import app_router
from fastapi import FastAPI, HTTPException
import secondcourse.app.model
from secondcourse.app.database.base import Base
from secondcourse.app.database.database import engine

# Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(app_router)