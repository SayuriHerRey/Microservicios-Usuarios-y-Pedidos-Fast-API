class PedidoService:

    def __init__(self, repository):
        self.repository = repository

    def crear_pedido(self, pedido):
        return self.repository.crear(pedido)

    def listar_pedidos(self):
        return self.repository.listar()

    def actualizar_pedido(self, id_pedido: int, pedido):
        return self.repository.actualizar(id_pedido, pedido)

    def eliminar_pedido(self, id_pedido: int):
        return self.repository.eliminar(id_pedido)
