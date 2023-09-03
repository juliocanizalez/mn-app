from pydantic import BaseModel
from typing import List, Optional


class NewtonRaphson(BaseModel):
    func: str
    x: float
    err: float
    logs: Optional[List[str]] = []
    timeSpent: Optional[str] = None
    iterations: Optional[int] = 100
