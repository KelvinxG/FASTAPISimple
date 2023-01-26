from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

#import UserMixin




class User(BaseModel):
    id:int 
    username:str
    password:str
    email:str
    phone:str



#initialize the app
app = FastAPI()


#add the routes to the app
@app.get('/')
def read_root():
    html_element="""
    <html>
        <body>
            <h1> Welcome to FastAPI,<a href='/createUser'> Create a User </a></h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_element,status_code=200)

@app.post('/createUser/')
async def create_user(users:User):
    return  users