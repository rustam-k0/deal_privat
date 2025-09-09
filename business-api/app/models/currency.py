from pydantic import BaseModel


class Currency(BaseModel):
    """
    Модель валюты
    """
    code: str
    name: str