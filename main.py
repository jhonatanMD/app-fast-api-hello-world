from fastapi import FastAPI

app = FastAPI()


@app.get("/get")
async def get():
    return {"message":"Hello World"}