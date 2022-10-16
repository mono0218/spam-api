import onnxruntime
from fastapi import FastAPI
import test

app = FastAPI()



@app.get("/")
async def root():
    return {"status": "active"}


@app.post("/post/{date}")
def post(date):
    req = date
    return {"result": "".join(test.mono(req))}
