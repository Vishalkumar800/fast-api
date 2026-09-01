from sqlalchemy import create_engine
from secondcourse.app.core.config import settings

engine = create_engine(
    settings.DATABASE_POSTGRES_HOST
)