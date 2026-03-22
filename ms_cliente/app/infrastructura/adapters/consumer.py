import pika
import json

from app.domain.user import User
from app.infrastructura.adapters.user_repository import MYSQLUserRepository

repository = MYSQLUserRepository()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='clientes')


def callback(ch, method, properties, body):

    mensaje = json.loads(body.decode())

    user = User(
        id_user=mensaje.get("id_user"),
        nombre=mensaje.get("nombre"),
        email=mensaje.get("email"),
        telefono=mensaje.get("telefono"),      # 👈 agregado
        direccion=mensaje.get("direccion")     # 👈 agregado
    )

    # guardar en MySQL
    repository.guardar(user)

    # generar archivo TXT
    archivo = f"user_{user.nombre}.txt"

    with open(archivo, "w") as f:
        f.write("REGISTRO DE USUARIO\n")
        f.write(f"Nombre: {user.nombre}\n")
        f.write(f"Email: {user.email}\n")

        # opcional pero mejor
        if user.telefono:
            f.write(f"Telefono: {user.telefono}\n")

        if user.direccion:
            f.write(f"Direccion: {user.direccion}\n")

    print(f"Usuario {user.nombre} guardado y archivo generado")


channel.basic_consume(
    queue='clientes',
    on_message_callback=callback,
    auto_ack=True
)

print("Esperando mensajes...")
channel.start_consuming()