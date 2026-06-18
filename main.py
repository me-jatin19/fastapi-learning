from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str

@app.post("/hello")
def say_hello(user: User):
    return {
        "message": f"Hello {user.name}"
    }