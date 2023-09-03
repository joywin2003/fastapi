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
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    gender:Optional[Gender] = None
    roles:Optional[List[Role]] = None
