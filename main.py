from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from api import api_class
from pydantic import BaseModel

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

obj = api_class()



class Item(BaseModel):
    name: str


@app.get('/')
def read_root():
    return 1

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/api/signin")
def read_root(username : str, password : str):
    print(username, password)
    return HTMLResponse(obj.sign_in("d", "z"))

@app.post("/api/signup")
def read_root():
    return HTMLResponse(obj.sign_up("d", "z", "vano"))
