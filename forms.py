
from pydantic import BaseModel

class CreateObject(BaseModel):
    city: str
    name_object:str
    user_id:int

class ReadObject(BaseModel):
    city: str
    name_object:str
    user_id:int

class UpdateObject(BaseModel):
    city:str
    name_object:str
    user_id:int

class DeleteObject(BaseModel):
    name_object:str







class CreateUser(BaseModel):
    user_name:str
    user_tg_id:int
    user_phone:int
    user_password:str
    user_post:str

class ReadUser(BaseModel):
    user_name:str
    user_tg_id:int
    user_phone:int
    user_post:str

class UpdateUser(BaseModel):
    user_name:str
    user_phone:int
    user_password:str
    user_post:str

class DeleteUser(BaseModel):
    user_name:str





class CreateQuery(BaseModel):
    user_id: int
    objact_id: int
    query_product: str
    quantity: int
    descreption: str


class CreateOrder(BaseModel):
    query_id:int
    article:str
    product:str
    price:int
    sale:int
    remains:int
