from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from api.models.biseccion import Biseccion
from api.services.biseccion_service import calc_biseccion

router = APIRouter()


@router.post("/biseccion", response_model=List[str])
def perform_calc_biseccion(data: Biseccion):
    res = calc_biseccion(data)
    return JSONResponse(content=res)
