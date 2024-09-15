from pydantic import BaseModel

class StudentBase(BaseModel):
    name:str
    age:int
    attendance:float
    standard:str

class StudentCreate(StudentBase):
    pass
class StudentUpdate(StudentBase):
    pass
class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode=True
        