import re
import ABM
import vizu 
import inspect
import matplotlib.pyplot as plt

def funcao(func):
    code = inspect.getsource(func)
    
    match = re.search(r"return (.*)", code)

    if match:
        return match.group(1)

def f(x, y):
    return -(x*y) + 1

def f1(x, y1, y2):
    return y2

def f2(x, y1, y2):
    return -2*y2 - 0.5*y1

x_abm, y_abm = ABM.uma_f(f, -1, 0, 1, 0.2)
x_abm2, y1_abm2, y2_abm2 = ABM.duas_f(f1, f2, 0, 1, 0, 1, 0.2)

print("Com uma EDO")
print("")
print("Função: ", funcao(f))
print("")

print("Método  Adams-Bashforth-Moulton: ")
print("Xs: ", x_abm)
print("Ys: ", y_abm)
print("")

print("")
print("*"*100)
print("")

print("Com duas EDOs")
print("")

print("Funções:\n F1: ", funcao(f1), "\n F2: ", funcao(f2))
print("")

print("Método  Adams-Bashforth-Moulton: ")
print("Xs: ", x_abm2)
print("Y1s: ", y1_abm2)
print("Y2s: ", y2_abm2)
print("")

vizu.abrir_graficos_ABM(x_abm, y_abm, x_abm2, y1_abm2, y2_abm2)