from fastapi import FastAPI,HTTPException
from modal import User, Gender, Role ,Update_User 
from typing import List
from uuid import uuid4,UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("8eb10e52-d0d4-459d-b799-041d78af29ef"),
        first_name="Joywin",
        middle_name= "shawn",
        last_name="Bennis",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("4119df7a-977f-4cc5-9026-8724c47277ef"),
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

@app.post("/api/v1/users/{user_id}")
async def register_user(updateuser:Update_User, user_id:UUID):
    for user in db:
        if user.id == user_id:
            if updateuser.first_name is not None:
                user.first_name = updateuser.first_name
            if updateuser.middle_name is not None:
                user.middle_name = updateuser.middle_name
            if updateuser.last_name is not None:
                user.last_name = updateuser.last_name
            if updateuser.gender is not None:
                user.gender = updateuser.gender
            if updateuser.roles is not None:
                user.roles = updateuser.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id does not exists"
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exists"
    )