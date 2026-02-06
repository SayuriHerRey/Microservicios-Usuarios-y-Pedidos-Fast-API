from pydantic import BaseModel

class Pedido(BaseModel):
    id_pedido: int
    id_user: int
    descripcion: str
