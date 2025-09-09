from fastapi import APIRouter
from typing import List
from app.models.currency import Currency

# Создаем роутер для валют
router = APIRouter()


@router.get("/currencies", summary="Получить список валют")
def get_currencies() -> List[Currency]:
    """
    Возвращает список поддерживаемых валют
    """
    return [
        Currency(code="USD", name="$"),
        Currency(code="EUR", name="€"),
        Currency(code="RUB", name="₽")
    ]