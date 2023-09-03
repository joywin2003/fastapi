from typing import Optional,List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    user = "user"
    admin = "admin"
    student = "student"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender:Gender
    roles:List[Role]
    
class Update_User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    gender:Optional[Gender]
    roles:Optional[List[Role]]
