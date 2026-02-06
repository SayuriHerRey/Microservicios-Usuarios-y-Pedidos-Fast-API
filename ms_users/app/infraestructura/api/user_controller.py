from fastapi import APIRouter
from domain.user import User
from application.services.user_service import UserService
from infraestructura.adapters.user_repository import UserRepositoryMemory

router = APIRouter()

repo = UserRepositoryMemory()
service = UserService(repo)

@router.post("/users")
def crear_user(user: User):
    return service.crear_user(user)

@router.get("/users")
def listar_users():
    return service.listar_users()

@router.get("/users/{id_user}")
def obtener_user(id_user: int):
    return service.obtener_user(id_user)

@router.put("/users/{id_user}")
def actualizar_user(id_user: int, user: User):
    return service.actualizar_user(id_user, user)

@router.delete("/users/{id_user}")
def eliminar_user(id_user: int):
    return service.eliminar_user(id_user)
