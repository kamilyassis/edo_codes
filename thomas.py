import numpy as np

def resolver_sistema_tridiagonal(A, B, x, y0, yf):

    print("\nResolvendo o sistema tridiagonal com Thomas...")

    n = len(B)-1

    #inicializando e extraindo diagonais
    a = np.zeros(n)  
    b = np.zeros(n)     
    c = np.zeros(n)  

    for i in range(n):

        b[i] = A[i, i]

        if i > 0:
            a[i] = A[i, i-1]
   
        if i < n - 1:
            c[i] = A[i, i+1]
    
    #eliminação
    for i in range(1, n):
        m = a[i] / b[i-1]
        b[i] -= m * c[i-1]
        B[i] -= m * B[i-1]

    #substituição regressiva
    y = np.zeros(n)
    y[-1] = B[-1] / b[-1]

    for i in range(n-2, -1, -1):
        y[i] = (B[i] - c[i] * y[i+1]) / b[i]

    #condições de contorno
    y_completo = np.zeros(len(x))
    if y0 is not None:
        y_completo[0] = y0
        y_completo[1:n+1] = y 
    else:
        y_completo[:n] = y
    
    if yf is not None:
        y_completo[-1] = yf
    return y_completo