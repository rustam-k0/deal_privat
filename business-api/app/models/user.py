from pydantic import BaseModel
from typing import Literal


class User(BaseModel):
    """
    Модель пользователя
    """
    id: int
    name: str
    role: Literal["MANAGER", "ACCOUNTANT"]