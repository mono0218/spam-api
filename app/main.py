from fastapi import FastAPI
from pydantic import BaseModel
import test

app = FastAPI()

class Data(BaseModel):
    name: str


@app.get("/")
async def root():
    return {"status": "active"}


@app.post("/post/")
def post(date: Data):
    req = date.name
    return {"result": "".join(test.mono(req))}
