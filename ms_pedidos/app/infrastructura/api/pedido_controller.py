from fastapi import APIRouter
from pydantic import BaseModel
import pika
import json
from app.domain.pedidos import Pedido
from app.application.service.pedido_service import PedidoService
from app.infrastructura.adapters.pedido_repository import POSTGRESPedidoRepository

router = APIRouter()

repo = POSTGRESPedidoRepository()
service = PedidoService(repo)

class Pedido(BaseModel):
    cliente_id: int
    producto: str
    cantidad: int
    estado: str

@router.post("/pedidos")
def crear_pedido(data: Pedido):

    mensaje = {
        "cliente_id": data.cliente_id,
        "producto": data.producto,
        "cantidad": data.cantidad,
        "estado": data.estado
    }

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')  
    )

    channel = connection.channel()

    channel.queue_declare(queue='pedidos')  

    channel.basic_publish(
        exchange='',
        routing_key='pedidos',
        body=json.dumps(mensaje)
    )

    connection.close()

    return {"mensaje": "Pedido enviado a RabbitMQ"}
    

@router.get("/pedidos")
def listar_pedidos():
    return service.listar_pedidos()


@router.put("/pedidos/{id_pedido}")
def actualizar_pedido(pedido:Pedido):
    return service.actualizar_pedido(id_pedido, pedido)


@router.delete("/pedidos/{id_pedido}")
def eliminar_pedido(id_pedido: int):
    return service.eliminar_pedido(id_pedido)