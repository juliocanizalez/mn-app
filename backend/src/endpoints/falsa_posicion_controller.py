from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from api.models.falsa_posicion import FalsaPosicion
from api.services.falsa_posicion_service import calc_falsa_posicion

router = APIRouter()


@router.post("/falsa-posicion", response_model=List[str])
def perform_calc_falsa_posicion(data: FalsaPosicion):
    res = calc_falsa_posicion(data)
    return JSONResponse(content=res)
