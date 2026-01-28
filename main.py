from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Float

app = FastAPI()
Base = declarative_base()

# SQLite setup
engine = create_engine("sqlite:///users.db")
SessionLocal = sessionmaker(bind=engine)

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

class ExerciseDB(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float, default=0.0)  # 0 jos kehonpaino

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    username: str
    email: str
    
class Exercise(BaseModel):
    name: str
    sets: int
    reps: int
    weight: float = 0.0  # 0 = kehonpaino

@app.post("/users")
def create_user(user: User):
    db = SessionLocal()
    db_user = UserDB(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return {"message": "user created", "user": user}

@app.get("/users")
def get_users():
    db = SessionLocal()
    all_users = db.query(UserDB).all()
    db.close()
    return all_users

@app.post("/exercises")
def create_exercise(exercise: Exercise):
    db = SessionLocal()
    db_exercise = ExerciseDB(
        name=exercise.name,
        sets=exercise.sets,
        reps=exercise.reps,
        weight=exercise.weight
    )
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    db.close()
    return {"message": "exercise created", "exercise": exercise}

@app.get("/exercises")
def get_exercises():
    db = SessionLocal()
    all_exercises = db.query(ExerciseDB).all()
    db.close()
    return all_exercises