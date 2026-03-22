class UserService:

    def __init__(self, repository):
        self.repository = repository

    def crear_user(self, user):
        return self.repository.crear(user)

    def listar_users(self):
        return self.repository.listar()

    def actualizar_user(self, id_user: int, user):
        return self.repository.actualizar(id_user, user)

    def eliminar_user(self, id_user: int):
        return self.repository.eliminar(id_user)
