from app.application.ports.pedido_repository import PedidoRepository
from app.domain.pedidos import Pedido

class PedidoRepositoryMemory(PedidoRepository):

    def __init__(self):
        self.pedidos = []

    def crear(self, pedido: Pedido):
        self.pedidos.append(pedido)
        return pedido

    def listar(self):
        return self.pedidos

    def actualizar(self, id_pedido: int, pedido: Pedido):
        for i, p in enumerate(self.pedidos):
            if p.id_pedido == id_pedido:
                self.pedidos[i] = pedido
                return pedido
        return None

    def eliminar(self, id_pedido: int):
        self.pedidos = [p for p in self.pedidos if p.id_pedido != id_pedido]
        return True
