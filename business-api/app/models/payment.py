from pydantic import BaseModel
from typing import Literal


class Payment(BaseModel):
    """
    Модель платежа
    """
    id: str
    amount: int
    currency: str
    status: Literal["PENDING", "CONFIRMED", "FAILED"]


class PaymentResponse(BaseModel):
    """
    Ответ при получении платежа (упрощенная версия)
    """
    id: str
    status: Literal["PENDING", "CONFIRMED", "FAILED"]
    amount: int