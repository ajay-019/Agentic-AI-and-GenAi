from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str
    email:EmailStr
    cgpa:float=Field(gt=0.0,lt=10.0,default=5,description='A decimal value representing the cgpa of the student')

new_student={'name':'Ajay','email':'abc@iitb.ac.in','cgpa':8.5}

student=Student(**new_student)

student_dict=dict(student)
print(student_dict['name'])

student_json =student.model_dump_json()
print(student_json)