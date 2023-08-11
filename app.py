from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    item_id: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def list_items():
    return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


@app.post("/items/")
async def create_item(item: Item):
    return item
