import numpy as np

def uma_pvc_robin(f, x0, xf, y0, h, k):
    print("\nCalculando o sistema com robin...")

    N = int((xf - x0) / h)
    x = np.linspace(x0, xf, N + 1)
    n = N  -1

    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(n):
        A[i, i] = -2 + h**2 * k
        if i > 0:
            A[i, i-1] = 1
        if i < n - 1:
            A[i, i+1] = 1
        B[i] = f(-5, k) * h**2  

    A[-1, -1] = -1 + h**2 * k  
    A[-1, -2] = 1
    B[-1] = f(-5, k) * h**2  

    B[0] -= y0

    print("Matriz A (Robin):\n", np.round(A, 3))
    print("\nVetor B (Robin):\n", np.round(B, 3))

    return A, B, x