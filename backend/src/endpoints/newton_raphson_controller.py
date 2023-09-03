from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from api.models.newton_raphson import NewtonRaphson
from api.services.newton_raphson_service import calc_newton_raphson

router = APIRouter()


@router.post("/newton-raphson", response_model=List[str])
def perform_cal_newton_raphson(data: NewtonRaphson):
    res = calc_newton_raphson(data)
    return JSONResponse(content=res)
