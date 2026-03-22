from fastapi import FastAPI
from app.infrastructura.api.user_controller import router

app = FastAPI(title="Microservicio Usuarios")
app.include_router(router)

# Ejecutar con:
# uvicorn main:app --port 8001 --reload
#http://localhost:8001/docs