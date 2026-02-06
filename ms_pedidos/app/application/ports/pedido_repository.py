from abc import ABC, abstractmethod
from domain.pedidos import Pedido

class PedidoRepository(ABC):

    @abstractmethod
    def crear(self, pedido: Pedido):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def eliminar(self, id_pedido: int):
        pass
