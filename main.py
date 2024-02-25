from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from api import db_api_class
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

obj = db_api_class()

obj.add_course(1, "course 0", "descriptions")

@app.get('/')
def read_root():
    obj.add_course(1, "course 0", "descriptions")
    return HTMLResponse(123)


@app.post("/api/signin")
def read_root(username : str, password : str):
    return HTMLResponse(obj.sign_in(username, password))

@app.post("/api/signup")
def read_root(username : str, name : str, password : str):
    return HTMLResponse(obj.sign_up(username, password, name))

@app.get("/api/getName")
def read_root(id : int):
    return HTMLResponse(obj.get_nick(id))

@app.get("/api/getRef")
def read_root(id : int):
    return HTMLResponse(obj.get_ref(id))

@app.get("/api/getCourses")
def read_root(id : int):
    return HTMLResponse(obj.get_courses(id))

@app.get("/api/getAllCourses")
def read_root():
    return HTMLResponse(obj.get_all_courses())

@app.get("/api/getImage")
def read_root(id : int):
    return HTMLResponse(obj.get_image(id))

@app.post("/api/addCourse")
def read_root(id : int, username : str, describtion : str):
    return HTMLResponse(obj.sign_up(id, username, describtion))

@app.post("/api/addTasktoCourse")
def read_root(id : int, statement : str, maxMark : int, deadline : str):
    return HTMLResponse(obj.sign_up(id, statement, maxMark, deadline))