import matplotlib.pyplot as plt

def grafico(x, y, titulo="não especificado", ax=None):

    if ax is None:
        ax = plt.gca() 

    ax.plot(x, y, label="y")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid()
    ax.set_title(titulo)

def grafico_2(x, y1, y2, titulo="não especificado", ax=None):

    if ax is None:
        ax = plt.gca() 

    ax.plot(x, y1, label='y1', color='blue') 
    ax.plot(x, y2, label='y2', color='red')     
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend() 
    ax.grid()
    ax.set_title(titulo)

def abrir_graficos(x_euler, y_euler, x_rk4, y_rk4, x_euler2, y1_euler2, y2_euler2, x_rk42, y1_rk42, y2_rk42):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8)) 
    axs = axs.flatten()  

    grafico(x_euler, y_euler, "Euler com uma EDO", axs[0])
    grafico(x_rk4, y_rk4, "RK4 com uma EDO", axs[1])
    grafico_2(x_euler2, y1_euler2, y2_euler2, "Euler com uma EDO", axs[2])
    grafico_2(x_rk42, y1_rk42, y2_rk42, "RK4 com uma EDO", axs[3])

    plt.tight_layout()
    plt.show()

def abrir_graficos_ABM(x_abm, y_abm, x_abm2, y1_abm2, y2_abm2):
    fig, axs = plt.subplots(1, 2, figsize=(10, 4)) 
    axs = axs.flatten()  

    grafico(x_abm, y_abm, "ABM", axs[0])
    grafico_2(x_abm2, y1_abm2, y2_abm2, "Sistema ABM", axs[1])

    plt.tight_layout()
    plt.show()
