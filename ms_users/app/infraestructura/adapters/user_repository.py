from application.ports.user_repository import UserRepository
from domain.user import User

class UserRepositoryMemory(UserRepository):

    def __init__(self):
        self.users = []

    def crear(self, user: User):
        self.users.append(user)
        return user

    def listar(self):
        return self.users

    def obtener(self, id_user: int):
        for u in self.users:
            if u.id_user == id_user:
                return u
        return None

    def actualizar(self, id_user: int, user: User):
        for i, u in enumerate(self.users):
            if u.id_user == id_user:
                self.users[i] = user
                return user
        return None

    def eliminar(self, id_user: int):
        self.users = [u for u in self.users if u.id_user != id_user]
        return True
