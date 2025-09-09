from fastapi import FastAPI
from app.api.routes import ping, users, currencies, payments


def create_app() -> FastAPI:
    """
    Фабрика для создания и настройки FastAPI приложения
    Возвращает настроенный экземпляр приложения
    """
    # Создаем основное приложение
    app = FastAPI(
        title="Business API",
        description="API для управления пользователями, валютами и платежами",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Подключаем все маршруты
    app.include_router(ping.router, tags=["Health Check"])
    app.include_router(users.router, tags=["Users"])  # Убрали prefix
    app.include_router(currencies.router, tags=["Currencies"])  # Убрали prefix
    app.include_router(payments.router, tags=["Payments"])  # Убрали prefix
    
    return app