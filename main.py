import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api import api_class

app = FastAPI()
obj = api_class()

a = "a"

obj.sign_up("e", "c", "d")
print(obj.sign_in("e", "c"))

@app.get("/")
def f():
    print(obj.get_id("e"))
    return HTMLResponse(f"1")

@app.post("/api/signup")
def f():
    obj.sign_up("z", "z", "z")
    return HTMLResponse("2")

