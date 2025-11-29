from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str

@app.post("/create-user")
def create_user(person:User):
    return {"message": f"user {person.name} is created!"}

@app.put("/update-user/{user_id}")
def update_user(user_id:int, user :User):
    return {
        "message": "User updated successfully",
        "user_id":user_id,
        "updated_data":user
    }

@app.delete("/delete-user/{user_id}")
def delete_user(user_id:int):
    return{"message ": f"{user_id} has been deleted!"}