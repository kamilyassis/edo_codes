import re
import vizu 
import inspect
import RK4 as RK4
import euler as euler

def funcao(func):
    code = inspect.getsource(func)
    
    match = re.search(r"return (.*)", code)

    if match:
        return match.group(1)

def f(x, y):
    return x*y +2

def f1(x, y1, y2):
    return -2*y1*y2 +0.5*y2

def f2(x, y1, y2):
    return 2*y1*y2 -0.5*y2

#ordem: (f, y0, x0, xf, h) e (f1, f2, y10, y20, x0, xf, h)
x_euler, y_euler = euler.uma_f(f, 0, 0, 1, 0.1)
x_euler2, y1_euler2, y2_euler2 = euler.duas_f(f1, f2, 0.9, 0.1, 0, 1, 0.2)

x_rk4, y_rk4 = RK4.uma_f(f, 0, 0, 1, 0.1)
x_rk42, y2_rk42, y1_rk42 = RK4.duas_f(f1, f2, 0.9, 0.1, 0, 1, 0.2)

print("Com uma EDO")
print("")
print("Função: ", funcao(f))
print("")

print("Euler com uma EDO: ")
print("Xs: ", x_euler)
print("Ys: ", y_euler)
print("")
print("Runge Kutta 4º Ordem com uma EDO: ")
print("Xs: ", x_rk4)
print("Ys: ", y_rk4)

print("")
print("*"*100)
print("")

print("Com duas EDOs")
print("")

print("Funções:\n F1: ", funcao(f1), "\n F2: ", funcao(f2))
print("")
print("Euler: ")
print("Xs: ", x_euler2)
print("Y1s: ", y1_euler2)
print("Y2s: ", y2_euler2)
print("")
print("Runge Kutta 4º Ordem: ")
print("Xs: ", x_rk42)
print("Y1s: ", y1_rk42)
print("Y2s: ", y2_rk42)

vizu.abrir_graficos(x_euler, y_euler, x_rk4, y_rk4, x_euler2, y1_euler2, y2_euler2, x_rk42, y1_rk42, y2_rk42)