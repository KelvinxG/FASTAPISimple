"""
main.py to run the application

"""
import uvicorn
from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse



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


if __name__ == '__main__':
    uvicorn.run(app,debug=True,port=8000)