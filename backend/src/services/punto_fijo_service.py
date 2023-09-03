from typing import List
import time
from math import ceil
from api.models.punto_fijo import PuntoFijo
from api.utils.utils import calc_operation


def calc_punto_fijo(item: PuntoFijo) -> List[str]:
    startTime = time.time()
    x = item.x

    for i in range(1, item.iterations):
        xi = calc_operation(item.func, x)
        error = abs((xi - x) / xi)
        print(error)
        item.logs.append(f"[ITERACION {i}][RESULTADOS]")
        item.logs.append(f"[x = {x}][g(x) = {xi}]")
        item.logs.append(f"[Error = {ceil(error * 100)}%]")

        if error < item.err:
            item.timeSpent = time.time() - startTime
            item.logs.append(f"[ENCONTRADO][RESULTADO FINAL]")
            item.logs.append(f"[RAIZ APROXIMADA = {x}]")
            item.logs.append(f"[Tiempo = {item.timeSpent:.4f}s]")
            return item.logs
        else:
            x = xi

    return item.logs
