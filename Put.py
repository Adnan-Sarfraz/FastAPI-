from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.put("/update-user/{user_id}")
def update_user(user_id:int, user: User):
    return {
        "message": "User updated successfully",
        "user_id":user_id,
        "updated_data":user
    }
