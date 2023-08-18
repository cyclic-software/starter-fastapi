from fastapi import FastAPI
from fastapi.responses import FileResponse
import google.auth.transport.requests
from google.oauth2 import service_account

from pydantic import BaseModel

app = FastAPI()

SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


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

@app.get("/get-access-token")
async def get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.

    :return: Access token.
    """
    credentials = service_account.Credentials.from_service_account_file(
        'service-account.json', scopes=SCOPES)
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    # make it an array to be able to use it in the header
    return {"status": 200, "credentials": credentials.token}
