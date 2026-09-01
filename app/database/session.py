from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread":False},
    echo=False # jitni bhi sql login hoga wo hamre terminal me show nhi krega
)

sessionLocal = sessionmaker(bind=engine , autoflush=False)