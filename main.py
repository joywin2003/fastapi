from fastapi import FastAPI,HTTPException
from modal import User, Gender, Role ,Update_User 
from typing import List
from uuid import uuid4,UUID

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

# @app.post("/api/v1/users")
# async def register_user(user:Update_User):
#     for db_user in db:
#         if user.id == 
#     db.append(user)
#     return {"id":user.id}


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