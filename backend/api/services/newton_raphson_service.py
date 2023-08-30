from typing import List
import time
from math import ceil
from api.models.newton_raphson import NewtonRaphson
from api.utils.utils import calc_operation, calc_derivative


def calc_newton_raphson(item: NewtonRaphson) -> List[str]:
    startTime = time.time()
    xi = item.x
    for i in range(1, item.iterations):
        fx = calc_operation(item.func, xi)
        fy = calc_derivative(item.func, xi)
        x = xi - fx / fy
        err = abs((x - xi) / x)
        # log to response
        item.logs.append(f"[ITERACION {i}]")
        item.logs.append(f"[xi = {xi}][x = {x}]")
        item.logs.append(f"[Error = {ceil(err * 100)}%]")

        # eval error
        if err > item.err:
            xi = x
        else:
            item.timeSpent = time.time() - startTime
            item.logs.append(f"[ENCONTRADO EN {i} ITERACIONES]")
            item.logs.append(f"[RAIZ APROXIMADA = {x}]")
            item.logs.append(f"[TIEMPO: {item.timeSpent:.4f}s]")
            return item.logs

    return item.logs
