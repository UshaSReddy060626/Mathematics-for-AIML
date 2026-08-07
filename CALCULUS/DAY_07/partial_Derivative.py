import sympy as sp
x, y = sp.symbols("x y")
f = x**2 + 3*x*y + y**2
print("Partial derivative w.r.t x:")
print(sp.diff(f, x))
print("Partial derivative w.r.t y:")
print(sp.diff(f, y))