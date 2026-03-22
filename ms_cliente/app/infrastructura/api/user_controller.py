from fastapi import APIRouter
from pydantic import BaseModel
import pika
import json
from app.application.services.user_service import UserService
from app.infrastructura.adapters.user_repository import MYSQLUserRepository



router = APIRouter()

repo = MYSQLUserRepository()
service = UserService(repo)

class User(BaseModel):
    id_user: int
    nombre: str
    email: str
    telefono: str
    direccion: str

@router.post("/users")

def crear_user(data: User):

    mensaje = {
        "id_user": data.id_user,
        "nombre": data.nombre,
        "email": data.email,
        "telefono": data.telefono,
        "direccion": data.direccion
    }

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='172.30.80.1') 
    )

    channel = connection.channel()

    channel.queue_declare(queue='clientes')  # cola de clientes

    channel.basic_publish(
        exchange='',
        routing_key='clientes',
        body=json.dumps(mensaje)
    )

    connection.close()

    return {"mensaje": "Usuario enviado a RabbitMQ"}


@router.get("/users")
def listar_users():
    return service.listar_users()


@router.put("/users/{id_user}")
def actualizar_user(user: User):
    return service.actualizar_user(id_user, user)


@router.delete("/users/{id_user}")
def eliminar_user(id_user: int):
    return service.eliminar_user(id_user)