from sympy import *

# create a variable label called 'x'
x = symbols('x')

eq = Eq(x**3 + 2*x**2 + 4*x + 8, 0)
print(eq)

solutions = solve(eq, x)
print(solutions)
