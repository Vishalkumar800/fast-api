from sqlalchemy.orm import sessionmaker
from secondcourse.app.database.database import engine
from secondcourse.app.database.base import Base

sessionLocal = sessionmaker(autoflush=False, bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db

    finally:
        db.close()

'''

Bas yield yahan DB session temporarily dene ke liye hai, aur kaam hone ke baad finally mein session close ho jata hai.

'''