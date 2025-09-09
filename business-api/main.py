from app.core.app import create_app

# Создаем экземпляр приложения
app = create_app()

# Точка входа для запуска приложения
if __name__ == "__main__":
    import uvicorn
    # Передаем приложение как строку импорта для поддержки reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)