from sympy import symbols, E, parse_expr
import math


def calc_operation(str_expr: str, xInput: float) -> float:
    x = symbols("x")

    str_expr = process_expression(str_expr)

    parsed_expression = parse_expr(str_expr)
    if "E" in str_expr:
        substitutionValues = {
            x: xInput,
            E: math.e,
        }
        result = parsed_expression.subs(substitutionValues)

    result = float(parsed_expression.subs(x, xInput))

    return result


def calc_derivative(str_expr: str, xInput: float) -> float:
    x = symbols("x")

    str_expr = process_expression(str_expr)

    parsed_expression = parse_expr(str_expr)
    if "E" in str_expr:
        substitutionValues = {
            x: xInput,
            E: E.diff(),
        }
        result = parsed_expression.diff(x).subs(substitutionValues)

    result = float(parsed_expression.diff(x).subs(x, xInput))

    return result


def process_expression(str_expr: str) -> str:
    if "e" in str_expr:
        str_expr = str_expr.replace("e", "E")
    if "^" in str_expr:
        str_expr = str_expr.replace("^", "**")
    if "sen" in str_expr:
        str_expr = str_expr.replace("sen", "sin")

    return str_expr
