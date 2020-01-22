# fastAPI: python class
from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum
from typing import List
from datetime import datetime

# receive a body from a PUT request
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = True
    description: str = None
    tax: float = None

# User class: basic attribs: id, signup_datetime, friends_list
class User(BaseModel):
    id: int
    signup_date: datetime = None
    friends: List[int] = []
    
class ModelName(str, Enum):
    alexnet: "alexnet"
    resnet: "resnet"
    lenet: "lenet"

# create an instance of the class FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# basic format: path, operation, func
@app.get("/")
# async def OR def; async: await available
def read_root():
    return {"Key": "Value"}

#path operation decorator
@app.get("/items/{item_id}")
# Query(None): serve the same purpose of defining the default value
#max_len:20; min_len:3
async def read_item(item_id: int, q: str = Query(None, max_length=20, min_length=3, regex="^999$")):
    return {"item_id": item_id, "q": q}

# get return value only if regex matched
@app.get("/items")
async def read_items(q: str = Query(None, max_length=15, regex="^999$")):
    results = {"items": [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]}
    return results


@app.get("/skiptest/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.post("/items/")
async def create_item(item_id: int, item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.tax + item.price
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict

@app.put("/items/{item
# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.
reveal_type(1)  # -> Revealed type is 'builtins.int'

# Use Union when something could be one of a few types
x: List[Union[int, str]] = [3, 5, "test", "fun"]

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
x: Any = mystery_function()

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing a type annotation
x: List[str] = []
x: Optional[str] = None

# This makes each positional arg and each keyword arg a "str"
def call(self, *args: str, **kwargs: str) -> str:
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)

# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to comment every "ignore" with a bug link
# (in mypy, typeshed, or your own code) or an explanation of the issue.
x = confusing_function()  # type: ignore  # https://github.com/python/mypy/issues/1167

# "cast" is a helper function that lets you override the inferred
# type of an expression. It's only for mypy -- there's no runtime check.
a = [4]
b = cast(List[int], a)  # Passes fine
c = cast(List[str], a)  # Passes fine (no runtime check)
reveal_type(c)  # -> Revealed type is 'builtins.list[builtins.str]'
print(c)  # -> [4]; the object is not cast

# If you want dynamic attributes on your class, have it override "__setattr__"
# or "__getattr__" in a stub or in your source code.
#
# "__setattr__" allows for dynamic assignment to names
# "__getattr__" allows for dynamic access to names
class A:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name: str, value: int) -> None: ...

    # This will allow access to any A.x, if x is compatible with the return type
    def __getattr__(self, name: str) -> int: ...

a.foo = 42  # Works
a.bar = 'Ex-parrot'  # Fails type checking_id}")
# declare type Item model to item
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}

# enum 
@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

# path: param should matches type of path
@app.get("/file/{file_path: path}")
def read_file_path():
    return {"file_path": file_path}


@app.get("/users/default")
async def read_default_user():
    return {"user_name": "default_user"}