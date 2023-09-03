from fastapi import FastAPI
from modal import User, Gender, Role  
from typing import List
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Joywin",
        middle_name= "shawn",
        last_name="Bennis",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name = "Joswin",
        # middle_name= "",
        last_name = "Bennis",
        gender = Gender.male,
        roles= [Role.student]    
    ),
]


@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.get("/api/v1/users")
async def fetch_user():
    return db;

@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id":user.id}