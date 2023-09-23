from RiemannSum import RiemannSum
from sympy import parse_expr

min_value = float(input("Informe o valor de a: "))
max_value = float(input("Informe o valor de b: "))
n = int(input("Informe o número de intervalos: "))
exp = parse_expr(input("Informe o f(x): "))
dx = (max_value - min_value)/n

riemannSum = RiemannSum(min_value, max_value, n, exp)

print("Soma de Riemann à esquerda:", riemannSum.resultLeft())
print("Soma de Riemann à direita:", riemannSum.resultRight())
print("O resultado da integral definida é:", riemannSum.resultIntegral())
