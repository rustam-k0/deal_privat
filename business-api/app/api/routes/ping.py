from fastapi import APIRouter

# Создаем роутер для проверки работоспособности
router = APIRouter()


@router.get("/ping", summary="Проверка работоспособности API")
def ping() -> str:
    """
    Простая проверка работы сервиса
    Возвращает "pong" если сервис работает
    """
    return "pong"