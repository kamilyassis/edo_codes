import numpy as np

def uma_pvc_newman(f, y0, x0, xf, h, k):
    print("\nCalculando o sistema com newman...")  

    N = int((xf - x0) / h)
    x = np.linspace(x0, xf, N + 1)
    n = N -1

    A = np.zeros((n, n))
    B = np.zeros(n)

    A[0, 0] = -1 + h**2 * k 
    A[0, 1] = 1

    for i in range(1, n - 1):
        A[i, i] = -2 + h**2 * k
        A[i, i-1] = 1
        A[i, i+1] = 1
        B[i] = f(-5, k) * h**2

    A[-1, -1] = -1 + h**2 * k  
    A[-1, -2] = 1
    B[0] -= y0
    B[-1] = f(-5, k) * h**2 - 0.2 * h  

    print("Matriz A (Newman):\n", np.round(A, 3))
    print("\nVetor B (Newman):\n", np.round(B, 3))

    return A, B, x