from pydantic import BaseModel
from typing import List, Optional


class FalsaPosicion(BaseModel):
    func: str
    aVal: float
    bVal: float
    err: float
    iterations: int
    logs: Optional[List[str]] = []
    timeSpent: Optional[str] = None
