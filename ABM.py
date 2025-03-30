import numpy as np
import RK4

def uma_f(f, y0, x0, xf, h):

    #rk4 usando x0 + h pq vai calcular só os 2 primeiros passos
    x_rk4, y_rk4 = RK4.uma_f(f, y0, x0, x0 + h, h)

    #inicializando arrays
    val_x = np.arange(x0, xf + h, h)
    val_y = np.zeros(len(val_x))
    val_y[:2] = y_rk4[:2] #recebe os 2 pontos já encontrados

    for i in range(2, len(val_x)):

        #preditor A-B
        y_preditor = val_y[i-1] + h/2 * (3 * f(val_x[i-1], val_y[i-1]) - f(val_x[i-2], val_y[i-2]))

        #corretor A-M
        val_y[i] = val_y[i-1] + h/12 * (5 * f(val_x[i], y_preditor) + 8 * f(val_x[i-1], val_y[i-1]) - f(val_x[i-2], val_y[i-2]))

    return val_x, val_y

def duas_f(f1, f2, y10, y20, x0, xf, h):

    x_rk4, y1_rk4, y2_rk4 = RK4.duas_f(f1, f2, y10, y20, x0, x0 + h, h)

    val_x = np.arange(x0, xf + h, h)
    val_y1 = np.zeros(len(val_x))
    val_y2 = np.zeros(len(val_x))
    val_y1[:2] = y1_rk4[:2]  #copia y1_0 e y1_1
    val_y2[:2] = y2_rk4[:2]  #copia y2_0 e y2_1

    for i in range(2, len(val_x)):

        #preditor A-B
        y1_pred = val_y1[i-1] + h/2 * (3 * f1(val_x[i-1], val_y1[i-1], val_y2[i-1]) - f1(val_x[i-2], val_y1[i-2], val_y2[i-2]))
        y2_pred = val_y2[i-1] + h/2 * (3 * f2(val_x[i-1], val_y1[i-1], val_y2[i-1]) - f2(val_x[i-2], val_y1[i-2], val_y2[i-2]))

        #corretor A-M
        val_y1[i] = val_y1[i-1] + h/12 * (5 * f1(val_x[i], y1_pred, y2_pred) + 8 * f1(val_x[i-1], val_y1[i-1], val_y2[i-1]) - f1(val_x[i-2], val_y1[i-2], val_y2[i-2]))
        val_y2[i] = val_y2[i-1] + h/12 * (5 * f2(val_x[i], y1_pred, y2_pred) + 8 * f2(val_x[i-1], val_y1[i-1], val_y2[i-1]) - f2(val_x[i-2], val_y1[i-2], val_y2[i-2]))

    return val_x, val_y1, val_y2