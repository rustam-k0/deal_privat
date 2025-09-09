from fastapi import APIRouter
from typing import List
from app.models.user import User

# Создаем роутер для пользователей
router = APIRouter()


@router.get("/users", summary="Получить список пользователей")
def get_users() -> List[User]:
    """
    Возвращает список всех пользователей системы
    """
    return [
        User(id=1, name="Ромочка", role="MANAGER"),
        User(id=2, name="Димочка", role="ACCOUNTANT")
    ]