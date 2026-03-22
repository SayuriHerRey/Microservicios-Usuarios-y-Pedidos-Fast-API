from app.application.ports.pedido_repository import PedidoRepository
from app.domain.pedidos import Pedido

class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def crear_pedido(self, pedido: Pedido):
        return self.repository.crear(pedido)

    def listar_pedidos(self):
        return self.repository.listar()

    def actualizar_pedido(self, id_pedido: int, pedido: Pedido):
        return self.repository.actualizar(id_pedido, pedido)

    def eliminar_pedido(self, id_pedido: int):
        return self.repository.eliminar(id_pedido)
