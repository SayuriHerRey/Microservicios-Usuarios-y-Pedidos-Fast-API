from fastapi import FastAPI
from app.infrastructura.api.pedido_controller import router

app = FastAPI(title="Microservicio Pedidos")
app.include_router(router)

# uvicorn main:app --port 8002 --reload
#http://localhost:8002/docs