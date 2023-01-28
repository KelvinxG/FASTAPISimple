"""

Models for ORM operations

"""

from .database import Base
from sqlalchemy import Boolean,Integer,String,ForeignKey,Column
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)
        
class Post(Base):
    __tablename__= 'posts'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))

    title = Column(String(100), nullable=False)

    

