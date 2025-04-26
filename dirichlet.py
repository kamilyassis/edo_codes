import numpy as np

def uma_pvc(f, x0, xf, y0, yf, c, h, k):
    print("\nCalculando o sistema com dirichlet...")

    #pontos
    N = int((xf - x0) / h)
    x = np.linspace(x0, xf, N + 1)

    #inicializando 
    n = N-1
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(n):

        #diagonal principal
        A[i, i] = -2 + h**2 *(k)

        #diagonal inferior
        if i > 0:
            A[i, i-1] = 1
        #diagonal superior
        if i < n - 1:
            A[i, i+1] = 1
        
        B[i] = f(c, k) * h**2

    B[0] -= y0
    B[-1] -= yf

    print("Matriz A:\n", np.round(A, 3))
    print("\nVetor B:\n", np.round(B, 3))
    
    '''
    A - matriz do sistema tridiagonal
    B - vetor de constantes
    x - pontos da malha
    '''

    return A, B, x