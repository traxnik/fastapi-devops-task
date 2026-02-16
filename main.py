from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/user")
def get_user(username: str):
    return {
        "username": username
    }


