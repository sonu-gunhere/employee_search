from pydantic import BaseModel
from typing import List, Optional


class Employee(BaseModel):
    name: str
    department: Optional[str] = None
    location: Optional[str] = None
    position: Optional[str] = None
