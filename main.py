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


@app.get('/')
def read_root():
    return 1


@app.post("/api/signin")
def read_root(username : str, password : str):
    return HTMLResponse(obj.sign_in(username, password))

@app.post("/api/signup")
def read_root(username : str, name : str, password : str):
    return HTMLResponse(obj.sign_up(username, password, name))

@app.get("/api/getName")
def read_root(id : int):
    return HTMLResponse(obj.get_nick(id))

@app.get("/api/getCourses")
def read_root(id : int):
    return HTMLResponse(obj.get_courses(id))

@app.get("/api/getAllCourses")
def read_root():
    return HTMLResponse(obj.get_all_courses())

@app.get("/api/getImage")
def read_root(id : int):
    return HTMLResponse(obj.get_image(id))