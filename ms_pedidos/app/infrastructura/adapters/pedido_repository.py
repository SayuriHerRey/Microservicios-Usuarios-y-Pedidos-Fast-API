import psycopg2

POSTGRES_HOST = "localhost"  

class POSTGRESPedidoRepository:

    def guardar(self, pedido):

        db = psycopg2.connect(
            host=POSTGRES_HOST,
            user="wslusuario1",
            password="123456",
            database="pedidos"
        )

        cursor = db.cursor()

        sql = """
        INSERT INTO pedidos (cliente_id, producto, cantidad, estado)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            pedido.cliente_id, 
            pedido.producto, 
            pedido.cantidad, 
            pedido.estado
        ))

        db.commit()

        cursor.close()
        db.close()

    def crear(self, pedido):

        db = psycopg2.connect(
            host=POSTGRES_HOST,
            user="wslusuario1",
            password="123456",
            database="pedidos"
        )

        cursor = db.cursor()

        sql = """
        INSERT INTO pedidos (cliente_id, producto, cantidad, estado)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """

        cursor.execute(sql, (
            pedido.id,
            pedido.cliente_id,
            pedido.producto,
            pedido.cantidad,
            pedido.estado
        ))

        pedido.id = cursor.fetchone()[0]

        db.commit()
        cursor.close()
        db.close()

        return pedido

    def listar(self):

        db = psycopg2.connect(
            host=POSTGRES_HOST,
            user="wslusuario1",
            password="123456",
            database="pedidos"
        )

        cursor = db.cursor()

        cursor.execute("SELECT * FROM pedidos")

        data = cursor.fetchall()

        cursor.close()
        db.close()

        return data

    def actualizar(self, id_pedido: int, pedido):

        db = psycopg2.connect(
            host=POSTGRES_HOST,
            user="wslusuario1",
            password="123456",
            database="pedidos"
        )

        cursor = db.cursor()

        sql = """
        UPDATE pedidos
        SET cliente_id=%s, producto=%s, cantidad=%s, estado=%s
        WHERE id=%s
        """

        cursor.execute(sql, (
            pedido.cliente_id,
            pedido.producto,
            pedido.cantidad,
            pedido.estado,
            id_pedido
        ))

        db.commit()
        cursor.close()
        db.close()

        return pedido

    def eliminar(self, id_pedido: int):

        db = psycopg2.connect(
            host=POSTGRES_HOST,
            user="wslusuario1",
            password="123456",
            database="pedidos"
        )

        cursor = db.cursor()

        cursor.execute("DELETE FROM pedidos WHERE id=%s", (id_pedido,))

        db.commit()
        cursor.close()
        db.close()

        return True