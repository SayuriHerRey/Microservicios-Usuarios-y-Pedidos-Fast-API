from application.ports.user_repository import UserRepository
from domain.user import User

class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def crear_user(self, user: User):
        return self.repository.crear(user)

    def listar_users(self):
        return self.repository.listar()

    def obtener_user(self, id_user: int):
        return self.repository.obtener(id_user)

    def actualizar_user(self, id_user: int, user: User):
        return self.repository.actualizar(id_user, user)

    def eliminar_user(self, id_user: int):
        return self.repository.eliminar(id_user)
