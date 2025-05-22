from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name : str = 'sangam'
    age : Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, le=10, default = 5, description="CGPA must be between 0 and 10")


new_student = {'age': 20, 'email': 'abc@gmail.com', 'cgpa': 8.5}
student = Student(**new_student)
print(student)

# python 5.StructuredOutput/pydantic_demo.py