from fastapi import APIRouter
from app.domain.pedidos import Pedido
from app.application.service.pedido_service import PedidoService
from app.infrastructura.adapters.pedido_repository import PedidoRepositoryMemory

router = APIRouter()

repo = PedidoRepositoryMemory()
service = PedidoService(repo)

@router.post("/pedidos")
def crear_pedido(pedido: Pedido):
    return service.crear_pedido(pedido)

@router.get("/pedidos")
def listar_pedidos():
    return service.listar_pedidos()

@router.put("/pedidos/{id_pedido}")
def actualizar_pedido(id_pedido: int, pedido: Pedido):
    return service.actualizar_pedido(id_pedido, pedido)


@router.delete("/pedidos/{id_pedido}")
def eliminar_pedido(id_pedido: int):
    return service.eliminar_pedido(id_pedido)
