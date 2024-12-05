from sympy import * 
x = Symbol('x')
expr = (x+3)**5
def fn(x):
c=1;
f=integrate(c*expr)
print(expr(1))
