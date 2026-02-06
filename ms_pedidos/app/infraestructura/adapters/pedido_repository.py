from application.ports.pedido_repository import PedidoRepository
from domain.pedidos import Pedido

class PedidoRepositoryMemory(PedidoRepository):

    def __init__(self):
        self.pedidos = []

    def crear(self, pedido: Pedido):
        self.pedidos.append(pedido)
        return pedido

    def listar(self):
        return self.pedidos

    def eliminar(self, id_pedido: int):
        self.pedidos = [p for p in self.pedidos if p.id_pedido != id_pedido]
        return True
