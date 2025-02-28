import numpy as np

def uma_f(f, y0, x0, xf, h):

    #arange vai criar os valores de x devidamente espaçados
    valores_x = np.arange(x0, xf + h, h)

    valores_y = np.zeros(len(valores_x))
    valores_y[0] = y0
    
    #iterar os valores de y, a partir de y1
    for i in range(1, len(valores_x)):
        valores_y[i] = valores_y[i-1] + h * f(valores_x[i-1], valores_y[i-1])
    
    return valores_x, valores_y

def duas_f(f1, f2, y10, y20, x0, xf, h):

    valores_x = np.arange(x0, xf + h, h)

    valores_y1, valores_y2 = np.zeros(len(valores_x)), np.zeros(len(valores_x))
    valores_y1[0], valores_y2[0] = y10, y20
    
    for i in range(1, len(valores_x)):
        x, y1, y2 = valores_x[i-1], valores_y1[i-1], valores_y2[i-1]
        valores_y1[i] = y1 + h * f1(x, y1, y2)
        valores_y2[i] = y2 + h * f2(x, y1, y2)
    
    return valores_x, valores_y1, valores_y2