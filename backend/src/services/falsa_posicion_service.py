from typing import List
import time
from math import ceil
from api.models.falsa_posicion import FalsaPosicion
from api.utils.utils import calc_operation


def calc_falsa_posicion(item: FalsaPosicion) -> List[str]:
    startTime = time.time()
    a = item.aVal
    b = item.bVal

    for i in range(1, item.iterations):
        fa = calc_operation(item.func, a)
        fb = calc_operation(item.func, b)

        xi = (a * fb - b * fa) / (fb - fa)
        fxi = calc_operation(item.func, xi)
        item.logs.append(f"[ITERACION {i}]")
        item.logs.append(f"[f(a): {fa}][f(b): {fb}][f(xi): {fxi}]")

        # calc error
        if i > 1:
            err = abs(xi - a)
            if xi > a and xi < b:
                a = xi

            item.logs.append(f"[xi: {xi}][err: {ceil(err * 100)}%]")
            if err < item.err:
                item.timeSpent = time.time() - startTime

                item.logs.append(f"[RAIZ ENCONTRADA EN {i} ITERACIONES]")
                item.logs.append(f"[{xi}]")
                item.logs.append(f"[Tiempo][{item.timeSpent:.4f}s]")

                return item.logs
        else:
            if xi > a and xi < b:
                a = xi
            item.logs.append(f"[xi: {xi}][err: N/A]")
    return item.logs
