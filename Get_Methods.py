from fastapi import FastAPI
#uvicorn main:app --reload

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Adnan! FastAPI is running."}

@app.get("/hello")
def say_hello():
    return {"message": "hello Adnan"}

@app.get("/hello/{name}")
def greet(name:str):
    return {"message":f"Hello {name}"}

@app.get("/square/{num}")
def square(num:int):
    return {"result": num*num }

@app.get("/User/{user_id}/Order/{order_id}")
def get_order(user_id:int, order_id:int):
    return {"user": user_id , "order": order_id}

@app.get("/add")
def add(a:int, b:int):
    return {"result": a+b}

@app.get("/users")
def get_users(role: str = "student", limit: int = 10):
    return {
        "role": role,
        "limit": limit
    }

