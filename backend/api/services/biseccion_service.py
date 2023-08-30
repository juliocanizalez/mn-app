from typing import List
import time
from math import ceil
from api.models.biseccion import Biseccion
from api.utils.utils import calc_operation


def calc_biseccion(item: Biseccion) -> List[str]:
    startTime = time.time()
    aVal = item.aVal
    bVal = item.bVal
    for i in range(1, item.iterations):
        midPoint = (aVal + bVal) / 2
        aExpr = bExpr = midExpr = item.func

        # missing eval function for each expr

        aFun = calc_operation(aExpr, aVal)
        bFun = calc_operation(bExpr, bVal)
        midFun = calc_operation(midExpr, midPoint)

        # calc error
        err = (bVal - aVal) / 2
        # log iteration
        item.logs.append(f"[ITERACION {i}][a = {aVal}][b = {bVal}][PM = {midPoint}]")
        item.logs.append(
            f"[RESULTADOS][f(a) = {aFun}][f(b) = {bFun}][f(PM) = {midFun}]"
        )
        item.logs.append(f"[Error = {ceil(err * 100)}%]")

        if (aFun * midFun) < 0:
            bVal = midPoint
        elif (aFun * midFun) > 0:
            aVal = midPoint
        elif (aFun * midFun) == 0:
            # log result
            timeSpent = time.time() - startTime
            item.timeSpent = f"{timeSpent:.4f}s"
            item.logs.append(f"[ENCONTRADO EN {i} ITERACIONES]")
            item.logs.append(f"[RAIZ APROXIMADA = {midPoint}]")
            item.logs.append(f"[Tiempo = {item.timeSpent}]")
            return item.logs

        if err > item.err:
            continue
        elif err < item.err:
            timeSpent = time.time() - startTime
            item.timeSpent = f"{timeSpent:.4f}s"
            item.logs.append(f"[ENCONTRADO EN {i} ITERACIONES]")
            item.logs.append(f"[RAIZ APROXIMADA = {midPoint}]")
            item.logs.append(f"[Tiempo = {item.timeSpent}]")
            return item.logs
