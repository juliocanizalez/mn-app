from fastapi import APIRouter
from api.controllers import *

router = APIRouter()

router.include_router(biseccion_router, prefix="", tags=["biseccion"])
router.include_router(newton_raphson_router, prefix="", tags=["newton-raphson"])
router.include_router(secante_router, prefix="", tags=["secante"])
router.include_router(falsa_posicion_router, prefix="", tags=["falsa-posicion"])
router.include_router(punto_fijo_router, prefix="", tags=["punto-fijo"])
