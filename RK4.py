import numpy as np

def uma_f(f, y0, x0, xf, h):

    valores_x = np.arange(x0, xf + h, h)
    valores_y = np.zeros(len(valores_x))
    valores_y[0] = y0
    
    for i in range(1, len(valores_x)):
        x, y = valores_x[i-1], valores_y[i-1]
        k1 = f(x, y)
        k2 = f(x + h/2, y + ((h/2) * k1))
        k3 = f(x + h/2, y + ((h/2) * k2))
        k4 = f(x + h, y + (h*k3))
        valores_y[i] = y + (h/6)*(k1 + 2*(k2 + k3) + k4)
    
    return valores_x, valores_y

def duas_f(f1, f2, y10, y20, x0, xf, h):

    valores_x = np.arange(x0, xf + h, h)
    valores_y1, valores_y2 = np.zeros(len(valores_x)), np.zeros(len(valores_x))
    valores_y1[0], valores_y2[0] = y10, y20
    
    for i in range(1, len(valores_x)):
        x, y1, y2 = valores_x[i-1], valores_y1[i-1], valores_y2[i-1]
        k1_y1 = f1(x, y1, y2)
        k1_y2 = f2(x, y1, y2)
        
        k2_y1 = f1(x + h/2, y1 + ((h/2) * k1_y1), y2 + ((h/2) * k1_y2))
        k2_y2 = f2(x + h/2, y1 + ((h/2) * k1_y1), y2 + ((h/2) * k1_y2))
        
        k3_y1 = f1(x + h/2, y1 + ((h/2) * k2_y1), y2 + ((h/2) * k2_y2))
        k3_y2 = f2(x + h/2, y1 + ((h/2) * k2_y1), y2 + ((h/2) * k2_y2))
        
        k4_y1 = f1(x + h, y1 + (h*k3_y1), y2 + (h*k3_y2))
        k4_y2 = f2(x + h, y1 + (h*k3_y1), y2 + (h*k3_y2))
        
        valores_y1[i] =  y1 + (h/6)*(k1_y1 + 2*(k2_y1 + k3_y1) + k4_y1)
        valores_y2[i] =  y2 + (h/6)*(k1_y2 + 2*(k2_y2 + k3_y2) + k4_y2)
    
    return valores_x, valores_y1, valores_y2
