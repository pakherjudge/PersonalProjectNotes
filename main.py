from fastapi import FastAPI

app = FastAPI() #create a FastAPI "instance"
# Here the app variable will be an "instance" of the class FastAPI.
# This will be the main point of interaction to create all your API.

@app.get("/") #decorator uses app instance and gets from path /
async def root(): 
    # It will be called by FastAPI whenever it receives 
    # a request to the URL "/" using a GET operation.

    return {"message": "Hello World"}
    # You can return a dict, list, singular values as str, int, etc.

# The value of the path parameter item_id will be passed to your function as the string argument item_id.
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# In this case, item_id is declared to be an int.
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

#define the specific user first in order, otherwise it thinks that /me is under /{user_id}
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# Similarly, you cannot redefine a path operation, The first one will always be used since the path matches first.
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]

# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]

from enum import Enum