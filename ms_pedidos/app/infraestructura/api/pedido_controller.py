from fastapi import APIRouter
from domain.pedidos import Pedido
from application.service.pedido_service import PedidoService
from infraestructura.adapters.pedido_repository import PedidoRepositoryMemory

router = APIRouter()

repo = PedidoRepositoryMemory()
service = PedidoService(repo)

@router.post("/pedidos")
def crear_pedido(pedido: Pedido):
    return service.crear_pedido(pedido)

@router.get("/pedidos")
def listar_pedidos():
    return service.listar_pedidos()

@router.delete("/pedidos/{id_pedido}")
def eliminar_pedido(id_pedido: int):
    return service.eliminar_pedido(id_pedido)
