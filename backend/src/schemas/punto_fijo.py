from pydantic import BaseModel
from typing import List, Optional


class PuntoFijo(BaseModel):
    func: str
    x: float
    err: float
    iterations: int
    logs: Optional[List[str]] = []
    timeSpent: Optional[str] = None
