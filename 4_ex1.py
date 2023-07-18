import numpy as np
import matplotlib.pyplot as plt 


def f(t):
    return (10*np.exp(-t)*np.sin(2*np.pi*t))**2 

def rectangulo(f, a, b, n):
    h = (b - a) / n
    integral = 0.0
    for i in range(n):
    	xi = a + h/2 + i*h
    	integral += f(xi)
    return h*integral
    
def trapezio(f, a, b, n):
    h = (b - a) / n
    integral2 = f(a)+f(b)
    for i in range(1,n):
        xi2 = a + i*h
        integral2 += 2 * f(xi2)
    integral2 *= h/2
    return integral2

def simpson(f, a, b, n):
    h = (b - a) / n
    integral3 = f(a) + f(b) 
    for i in range(1,n):
        xi = a + i*h
        if i%2 == 0:
            integral3 += 2 * f(xi)
        else:
            integral3 += 4 * f(xi)  
    integral3 *= h/3
    return integral3

erro_desejado = 0.0001
a = 0
b = 1/2
valor_exato = 15.41260804810169
M = 3250.7889

method = input("Qual o método que deseja utilizar?\n1. Rectangulo \n2. Trapézio \n3. Simpson \nDigite o número correspondente: ")

while method not in ['1', '2', '3']:
    method = input("Método inválido. Tente novamente.\nQual o método que deseja utilizar?\n1. Rectangulo \n2. Trapézio \n3. Simpson \nDigite o número correspondente: ")

if method == '1':
    n = int(input("Digite o número de iterações: "))
    result = rectangulo(f,a,b,n)
    n_rect = 1
    erro = 1 + erro_desejado
    while erro > erro_desejado:
        n_rect += 1
        erro = M * (b - a)**3 / (24 * n_rect**2)
    print("Integral =", result)  
    print(f"Para a regra do retangulo, n = {n_rect} para se obter o erro de {erro_desejado}")
    show_graph = input("Deseja visualizar o gráfico? (s/n): ").lower()
    while show_graph not in ['s', 'n']:
        show_graph = input("Deseja visualizar o gráfico? (s/n): ").lower()
    if show_graph.lower() == "s":
        x = np.linspace(a, b)
        y = f(x)
        plt.plot(x, y, label='f(t)')
        dx = (b - a) / n
        for i in range(n):
            xi = a + i*dx + dx/2
            plt.fill_between([xi - dx/2, xi + dx/2], [0, 0], [f(xi), f(xi)], color='r', alpha=0.3)
        plt.title('Regra do Rectangulo')
        plt.legend()
        plt.show()
    else:
        print("Se desejar ver o gráfico volte a correr o programa.")
elif method == '2':
    n = int(input("Digite o número de iterações: "))
    n_trap = 1
    erro = 1 + erro_desejado
    while erro > erro_desejado:
        n_trap += 1
        erro = M * (b - a)**3 / (12 * n_trap**2)
    result2 = trapezio(f,a,b,n)
    print("Integral =", result2)
    print(f"Para a regra do trapézio, n = {n_trap} para se obter o erro de {erro_desejado}")
    show_graph = input("Deseja visualizar o gráfico? (s/n): ").lower()
    while show_graph not in ['s', 'n']:
        show_graph = input("Deseja visualizar o gráfico? (s/n): ").lower()
    if show_graph.lower() == "s":
        x = np.linspace(a, b)
        y = f(x)
        plt.plot(x, y, label='f(t)')
        dx = (b - a) / n
        for i in range(n):
            xi = a + i*dx
            plt.fill_between([xi,xi+dx],[0,0], [f(xi), f(xi + dx)], color = 'r', alpha=0.3)
        plt.title('Regra do Trapézio')
        plt.legend()
        plt.show()
    else:
        print("Se desejar ver o gráfico volte a correr o programa.")
else:
    n = int(input("Digite o número de iterações: "))
    n_sim = 1
    erro = 1 + erro_desejado
    while erro > erro_desejado:
        n_sim += 1
        erro = M * (b - a)**5 / (180 * n_sim**4)
    result3 = simpson(f,a,b,n)
    print("Integral =", result3)
    print(f"Para a regra de Simpson, n = {n_sim} para se obter o erro de {erro_desejado}")
    show_graph = input("Deseja visualizar o gráfico? (s/n): ").lower()
    while show_graph not in ['s', 'n']:
        show_graph = input("Deseja visualizar o gráfico? (s/n): ").lower()
    if show_graph.lower() == "s":
        x = np.linspace(a, b)
        y = f(x)
        plt.plot(x, y, label='f(t)')
        dx = (b - a) / n
        for i in range(n):
            xi = a + i*dx
            if i % 2 == 0:
                plt.fill_between([xi, xi+dx], [0, 0], [f(xi), f(xi + dx)], color='r', alpha=0.3)
            else:
                plt.fill_between([xi, xi+dx], [0, 0], [f(xi), f(xi + dx)], color='g', alpha=0.3)
        plt.title('Regra de Simpson')
        plt.legend()
        plt.show()
    else: 
        print("Se desejar ver o gráfico volte a correr o programa.")
