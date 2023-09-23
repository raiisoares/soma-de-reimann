import sympy
from sympy import symbols

x = symbols("x")

class RiemannSum:
    def __init__(self, min_value, max_value, n, exp):
        self.min_value = min_value
        self.max_value = max_value
        self.n = n
        self.exp = exp
        self.dx = (max_value - min_value) / n

    def resultLeft(self):
        reimann_sum_left = 0.0
        for i in range(self.n):
            current_x = self.min_value + i * self.dx
            fx = self.exp.subs(x, current_x)
            reimann_sum_left += fx * self.dx
        return reimann_sum_left

    def resultRight(self):
        reimann_sum_right = 0.0
        for i in range(1, self.n + 1):
            current_x = self.min_value + i * self.dx
            fx = self.exp.subs(x, current_x)
            reimann_sum_right += fx * self.dx
        return reimann_sum_right

    def resultIntegral(self):
        return sympy.integrate(self.exp, (x, self.min_value, self.max_value))