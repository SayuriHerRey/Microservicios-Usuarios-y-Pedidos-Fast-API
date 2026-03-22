import pika
import json
from app.domain.pedidos import Pedido
from app.infrastructura.adapters.pedido_repository import POSTGRESPedidoRepository

repository = POSTGRESPedidoRepository()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()

channel.queue_declare(queue='pedidos')


def callback(ch, method, properties, body):

    mensaje = json.loads(body.decode())

    pedido = Pedido(
        cliente_id=mensaje.get("cliente_id"),
        producto=mensaje.get("producto"),
        cantidad=mensaje.get("cantidad"),
        estado=mensaje.get("estado")
    )

    # guardar en MySQL
    repository.guardar(pedido)

    # generar archivo TXT
    archivo = f"pedido_{pedido.cliente_id}.txt"

    with open(archivo, "w") as f:
        f.write("REGISTRO DE PEDIDO\n")
        f.write(f"Cliente ID: {pedido.cliente_id}\n")
        f.write(f"Producto: {pedido.producto}\n")
        f.write(f"Cantidad: {pedido.cantidad}\n")
        f.write(f"Estado: {pedido.estado}\n")

    print(f"Pedido {pedido.cliente_id} guardado y archivo generado")


channel.basic_consume(
    queue='pedidos',
    on_message_callback=callback,
    auto_ack=True
)

print("Esperando mensajes...")
channel.start_consuming()