from abc import ABC, abstractmethod
from app.domain.pedidos import Pedido

class PedidoRepository(ABC):

    @abstractmethod
    def crear(self, pedido):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def actualizar(self, id_pedido: int, pedido):
        pass

    @abstractmethod
    def eliminar(self, id_pedido: int):
        pass
