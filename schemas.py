from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
from datetime import datetime


class User(BaseModel):
    id: int
    username: str
    email: str

    def __str__(self) -> str:
        return f'id: {self.id}, username: {self.username}, email: {self.email}'

class Courses(BaseModel):
    course_id: int
    course_name: str
    course_description: str
    created_at: datetime
    price: float or str

class Students(BaseModel):
    student_id: int
    student_name: str
    student_email: str
    course_enrollment: int
    created_at: datetime
    course_id: int


    def __str__(self) -> str:
        return f'course_id: {self.course_id},name'
