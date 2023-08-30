from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from api.models.secante import Secante
from api.services.secante_service import calc_secante

router = APIRouter()


@router.post("/secante", response_model=List[str])
def perform_calc_secante(data: Secante):
    res = calc_secante(data)
    return JSONResponse(content=res)
