import numpy as np
import re, vizu, inspect
import newman 
import robin 
import thomas
import dirichlet as df

def funcao(func):
    code = inspect.getsource(func)
    
    match = re.search(r"return (.*)", code)

    if match:
        return match.group(1)

def f(c, k):
    return k*(c)

##exemplo para DF
x0, xf = 0, 1.5
y0, yf = 28, -5
c, h, k = -5, 0.25, 0.13

#ordem: (f, x0, xf, y0, yf, h)
A, B, x = df.uma_pvc(f, x0, xf, y0, yf, c, h, k)
y = thomas.resolver_sistema_tridiagonal(A, B, x, y0, yf)

print("Solução DF:")
print("  x      F(x)     ")
for xi, yi in zip(x, y):
    print(f"{xi:.2f}  {yi:.3f}")

# Robin
A_robin, B_robin, x_robin = robin.uma_pvc_robin(f, x0, xf, y0, h, k)
y_robin = thomas.resolver_sistema_tridiagonal(A_robin, B_robin, x_robin, y0=y0, yf=None)

print("Solução Robin:")
print("  x      F(x)     ")
for xi, yi in zip(x_robin, y_robin):
    print(f"{xi:.2f}  {yi:.3f}")

# Newman
A_newman, B_newman, x_newman = newman.uma_pvc_newman(f, y0, x0, xf, h, k)
y_newman = thomas.resolver_sistema_tridiagonal(A_newman, B_newman, x_newman, y0=None, yf=None)

print("Solução Newman:")
print("  x      F(x)     ")
for xi, yi in zip(x_newman, y_newman):
    print(f"{xi:.2f}  {yi:.3f}")
