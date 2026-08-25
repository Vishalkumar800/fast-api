from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.orm import sessionmaker , declarative_base , Session
from fastapi import FastAPI , Depends , HTTPException

# orm ka use krke sql query bina likhe python code dwara excute kra skhta ho 
app = FastAPI()


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):

    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True , index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind = engine)

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "message": "DB connected fine"
    }

"""
Session = database ke saath tumhare kaam ko manage karne wala object.
Just like manager that handle things

`Transaction` :  database me kiye ja rahe related changes ka ek group, jise ek saath save ya cancel kiya ja sakta hai.

Example : 
     
    Transaction start
      ↓
    Todo add
      ↓
    Todo update
      ↓
    Todo delete
      ↓
    COMMIT()

"""
@app.post("/todos")
def create_todo(title:str , db:Session = Depends(get_db)):
    todo = Todo(title = title , completed = "False" )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo Created",
        "data" : todo

    }



"""

------ Commit -----
Jo changes maine is transaction me kiye hain, unko final/save kar do.

db.add(todo)
      ↓
Session me pending
      ↓
db.commit()
      ↓
flush
      ↓
SQL database ko bheji
      ↓
transaction COMMIT
      ↓
Changes final ✅

"""
""" 

--------- Flush -----------
Man lo kuch data add kiya ya delete ab jo database me update krna hai wo flush() hi database ko
inform krega ki bhai essa krna hai .

Session
  ↓
Changes pending
  ↓
flush()
  ↓
Database: "Okay, INSERT/UPDATE/DELETE execute kar diya"
  ↓
commit()
  ↓
"Okay, changes final hain" ✅

"""

## Read All Data

@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return {
        "message": len(todos),
        "data" : todos
    }

@app.get("/todos/{todo_id}")
def query_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


#update data 
@app.patch("/todos/{todo_id}")
def update_todo(todo_id : int , title:str , db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo Not Found"
        )

    todo.title = title

    db.commit() # Note : jb kuch change krte hai toh commit krna pdta hai 
    db.refresh(todo)


    return {
        "message" : "Todo Updated",
        "data" : todo
    }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db : Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "message" : "Todo Deleted",
        "data" : todo
    }


