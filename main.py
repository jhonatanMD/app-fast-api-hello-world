from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI, Query
from fastapi import Body

app = FastAPI()


# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/get")
async def get():
    return {"message": "Hello World"}

#Body
@app.post("/person/new")
async def create_person(person: Person = Body(...)):
    return person

#QueryParam
@app.get("/person/detail")
async def show_person(
        name: Optional[str] = Query(None, min_length=1, max_length=50 , title="Parametro de nombre de la persona"),
        age: int = Query(... , title="Parametro de edad de la persona")
):
    return {name: age}
