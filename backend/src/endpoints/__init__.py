from .biseccion_controller import router as biseccion_router
from .newton_raphson_controller import router as newton_raphson_router
from .falsa_posicion_controller import router as falsa_posicion_router
from .punto_fijo_controller import router as punto_fijo_router
from .secante_controller import router as secante_router

__all__ = [
    "biseccion_router",
    "newton_raphson_router",
    "falsa_posicion_router",
    "punto_fijo_router",
    "secante_router",
]
