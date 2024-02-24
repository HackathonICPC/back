from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from api import api_class

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

a = "a"

# obj.sign_up("e", "c", "d")
# print(obj.sign_in("e", "c"))

# @app.get("/")
# async def f():
#     print(obj.get_id("e"))
#     return HTMLResponse(f"1")

@app.post("/api/signup")
def f():
     obj.sign_up("x", "x", "x")
     return HTMLResponse("3")

@app.post("/api/signin")
def f():
     obj.sign_in("x", "x", "x")
     return HTMLResponse("3")

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}
