from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    username: str
    email: str

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