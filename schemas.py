"""

schemas is for data validation


"""

from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    email: str

    def __str__(self) -> str:
        return f'id: {self.id}, username: {self.username}, email: {self.email}'

class Instructors(BaseModel):
    instructor_id: int
    instructor_name: str
    instructor_email: str
    created_at: datetime
    updated_at: datetime

    def __str__(self) -> str:
        return f'instructor_id: {self.instructor_id}, instructor_name: {self.instructor_name}, instructor_email: {self.instructor_email}, created_at: {self.created_at}, updated_at: {self.updated_at}'

class Courses(BaseModel):
    course_id: int
    course_name: str
    course_description: str
    created_at: datetime
    price: float or str

    def __str__(self) -> str:
        return f'course_id: {self.course_id}, {self.course_name}, {self.course_description}, {self.created_at}, {self.price}'

class Students(BaseModel):
    student_id: int
    student_name: str
    student_email: str
    course_enrollment: int
    created_at: datetime
    course_id: int


    def __str__(self) -> str:
        return f'course_id: {self.course_id},name'
