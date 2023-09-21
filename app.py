
import sympy
from sympy import parse_expr, symbols

x = symbols("x")

reimann_sum_left = 0.0
reimann_sum_right = 0.0

min_value = float(input("Informe o valor de a: "))
max_value = float(input("Informe o valor de b: "))
n = int(input("Informe o número de intervalos: "))
exp = parse_expr(input("Informe o f(x): "))
dx = (max_value - min_value)/n

for i in range(n):
    current_x = min_value + i * dx
    fx = exp.subs(x, current_x)
    reimann_sum_left += fx * dx

for i in range(1, n + 1):
    current_x = min_value + i * dx
    fx = exp.subs(x, current_x)
    reimann_sum_right += fx * dx

integral = sympy.integrate(exp, (x, min_value, max_value))

print("Soma de Riemann à esquerda:", round(reimann_sum_left, 4))
print("Soma de Riemann à direita:", round(reimann_sum_right, 4))
print("O resultado da integral definida é:", round(integral, 4))
