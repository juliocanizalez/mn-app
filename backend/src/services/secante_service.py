from typing import List
import time
from math import ceil
from api.models.secante import Secante
from api.utils.utils import calc_operation


def calc_secante(item: Secante) -> List[str]:
    if item.isModified:
        return calc_secante_modificada(item)
    else:
        return calc_secante_normal(item)


def calc_secante_normal(item: Secante) -> List[str]:
    startTime = time.time()
    x_0 = item.x
    x_1 = item.xPrev

    for i in range(1, item.iterations):
        fx_0 = calc_operation(item.func, x_0)
        fx_1 = calc_operation(item.func, x_1)
        xi = x_0 - (fx_0 * (x_1 - x_0)) / (fx_1 - fx_0)

        err = abs((xi - x_0) / xi)

        item.logs.append(f"[Iteracion {i}]")
        item.logs.append(f"[Raiz aprox = {xi}]")
        item.logs.append(f"[Error = {ceil(err * 100)}%]")

        if err < item.err:
            item.timeSpent = time.time() - startTime
            item.logs.append(f"[RAIZ ENCONTRADA EN {i} ITERACIONES]")
            item.logs.append(f"[Raiz aprox = {xi}]")
            item.logs.append(f"[Tiempo: {item.timeSpent:.4f}s]")

            return item.logs
        else:
            x_1 = x_0
            x_0 = xi

    return item.logs


def calc_secante_modificada(item: Secante) -> List[str]:
    startTime = time.time()
    x = item.x
    delta = item.delta

    for i in range(1, item.iterations):
        fx = calc_operation(item.func, x)
        delta_x = delta * x
        x_plus_delta = x + delta_x
        fx_plus_delta = calc_operation(item.func, x_plus_delta)

        xi = x - (fx * delta * x) / (fx_plus_delta - fx)

        # calc error
        err = abs((xi - x) / xi)

        # time to log
        item.logs.append(f"[Iteracion {i}]")
        item.logs.append(f"[Raiz aprox = {xi}]")
        item.logs.append(f"[Error = {ceil(err * 100)}%]")

        if err < item.err:
            item.timeSpent = time.time() - startTime
            # success
            item.logs.append(f"[RAIZ ENCONTRADA EN {i} ITERACIONES]")
            item.logs.append(f"[Raiz aprox = {xi}]")
            item.logs.append(f"[Tiempo: {item.timeSpent:.4f}s]")
            return item.logs
        else:
            x = xi

    return item.logs
