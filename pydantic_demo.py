from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    Name: str = "Ankit"
    Age: Optional[int] = None
    email: EmailStr
    CGPA: float = Field(
        gt=0,
        lt=10,
        default=5,
        description="A decimal value representing the CGPA of the student",
    )


# new_student = {"Age": 26, "email": "abc@gmail.com", "CGPA": 5}
new_student = {"Age": 26, "email": "abc@gmail.com"}
student = Student(**new_student)

student_dict = dict(student)

print(student_dict["Age"])
student_json = student.model_dump_json()

# print(student)
