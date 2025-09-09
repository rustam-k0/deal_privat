from fastapi import APIRouter
from app.models.payment import Payment, PaymentResponse

# Создаем роутер для платежей
router = APIRouter()


@router.post("/payments", summary="Создать новый платеж")
def create_payment() -> Payment:
    """
    Создает новый платеж со статусом PENDING
    """
    return Payment(
        id="P-2024-001",
        amount=1000,
        currency="USD", 
        status="PENDING"
    )


@router.get("/payments/{payment_id}", summary="Получить информацию о платеже")
def get_payment(payment_id: str) -> PaymentResponse:
    """
    Возвращает информацию о конкретном платеже по его ID
    """
    return PaymentResponse(
        id=payment_id,
        status="CONFIRMED",
        amount=1000
    )