import mysql.connector

MYSQL_HOST = "172.30.80.1 " 

class MYSQLUserRepository:

    def guardar(self, user):

        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user="wslusuario1",
            password="123456",
            database="clientes"
        )

        cursor = db.cursor()

        sql = """
        INSERT INTO clientes (nombre, email, telefono, direccion)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql,(user.nombre, user.email, user.telefono, user.direccion))

        db.commit()

        cursor.close()
        db.close()

    def crear(self, user):

        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user="wslusuario1",
            password="123456",
            database="clientes"
        )

        cursor = db.cursor()

        sql = """
        INSERT INTO clientes (nombre, email, telefono, direccion)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            user.nombre,
            user.email,
            user.telefono,
            user.direccion
        ))

        db.commit()

        cursor.close()
        db.close()

        return user


    def listar(self):

        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user="wslusuario1",
            password="123456",
            database="clientes"
        )

        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM clientes")

        data = cursor.fetchall()

        cursor.close()
        db.close()

        return data


    def actualizar(self, id_user: int, user):

        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user="wslusuario1",
            password="123456",
            database="clientes"
        )

        cursor = db.cursor()

        sql = """
        UPDATE clientes
        SET nombre=%s, email=%s, telefono=%s, direccion=%s
        WHERE id=%s
        """

        cursor.execute(sql, (
            user.nombre,
            user.email,
            user.telefono,
            user.direccion,
            id_user
        ))

        db.commit()

        cursor.close()
        db.close()

        return user


    def eliminar(self, id_user: int):

        db = mysql.connector.connect(
            host=MYSQL_HOST,
            user="wslusuario1",
            password="123456",
            database="clientes"
        )

        cursor = db.cursor()

        cursor.execute("DELETE FROM clientes WHERE id=%s", (id_user,))

        db.commit()

        cursor.close()
        db.close()

        return True