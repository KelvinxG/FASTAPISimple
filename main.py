"""
main.py to run the application

"""
import uvicorn
from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

from database import Base,sessionmaker,engine #database connection

from models import InstructorsModel,UserModel,UserModel # data models

from schemas import Instructors,User,Courses #data validation

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
session = SessionLocal()

#initialize the app
app = FastAPI()


#cruds

#get all the intructors from instructors model
@app.get('/api/instroctors/')
def get_instructors():
    instructors = Instructors()
    if instructors is None:
        return {"message": "No instructors found"}
    else:
        return instructors.get_all_instructors()
#post / create a new instructor
@app.post('/api/instructors/')
def create_instructor(instructor:Instructors):
    pass


@app.post('/createUser',response_model=User)
async def create_user(user:User):
    user=User(username=user.username,email=user.email)
    session.add(user)
    session.commit()
    return user
    

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


if __name__ == '__main__':
    uvicorn.run(app,debug=True,port=8000)