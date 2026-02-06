from application.ports.pedido_repository import PedidoRepository
from domain.pedidos import Pedido

class PedidoService:

    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def crear_pedido(self, pedido: Pedido):
        return self.repository.crear(pedido)

    def listar_pedidos(self):
        return self.repository.listar()

    def eliminar_pedido(self, id_pedido: int):
        return self.repository.eliminar(id_pedido)
