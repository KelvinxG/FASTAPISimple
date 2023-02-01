"""

Models for ORM operations and define database relationships

"""

from database import Base
from sqlalchemy import Boolean,Integer,String,ForeignKey,Column
from sqlalchemy.orm import relationship

#User
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

class Instructors(Base):
    __tablename__ = 'instructors'
    instructor_id = Column(Integer, primary_key=True)
    instructor_name = Column(String(20), nullable=False)
    instructor_email = Column(String(20), nullable=False)
    instructor_phone = Column(String(20), nullable=False)
    course_available = Column(String(20), nullable=False)


        
class Students(Base):
    __tablename__ ='students'
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(20), nullable=False)
    student_email = Column(String(20), nullable=False)
    student_phone = Column(String(20), nullable=False)
    class_enrollment = Column(String(20), nullable=False)




class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(20), nullable=False)
    course_code = Column(String(20), nullable=False)
    course_description = Column(String(200), nullable=False)
    instructor_id = Column(Integer, ForeignKey('instructors.instructor_id'))
    students = relationship('Students', backref='courses')

