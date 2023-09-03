from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from api.models.punto_fijo import PuntoFijo
from api.services.punto_fijo_service import calc_punto_fijo

router = APIRouter()


@router.post("/punto-fijo", response_model=List[str])
def perform_calc_punto_fijo(data: PuntoFijo):
    res = calc_punto_fijo(data)
    return JSONResponse(content=res)
