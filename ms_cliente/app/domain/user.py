from pydantic import BaseModel

class User(BaseModel):
    id_user: int
    nombre: str
    email: str
