class Pedido:
    def __init__(self, cliente_id, producto, cantidad, estado="pendiente"):
        self.cliente_id = cliente_id
        self.producto = producto
        self.cantidad = cantidad
        self.estado = estado