from abc import ABC, abstractmethod
from app.domain.user import User

class UserRepository(ABC):

    @abstractmethod
    def crear(self, user: User):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def actualizar(self, id_user: int, user: User):
        pass

    @abstractmethod
    def eliminar(self, id_user: int):
        pass
