from pydantic import BaseModel
from typing import List, Optional


class Secante(BaseModel):
    func: str
    x: float
    err: float
    iterations: int
    isModified: bool
    xPrev: Optional[float] = None
    delta: Optional[float] = None
    logs: Optional[List[str]] = []
    timeSpent: Optional[str] = None
