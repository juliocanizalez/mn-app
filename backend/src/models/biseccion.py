from pydantic import BaseModel
from typing import List, Optional


class Biseccion(BaseModel):
    func: str
    aVal: float
    bVal: float
    iterations: int
    err: float
    logs: Optional[List[str]] = []
    timeSpent: Optional[str] = None
    midPoint: Optional[float] = None
