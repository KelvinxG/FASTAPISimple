from pydantic import BaseModel

#pydantic 

#user model
class User(BaseModel):
    id:int
    name:str
    email:str
    password:str
    phone:str


