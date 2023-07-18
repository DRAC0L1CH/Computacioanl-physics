""" Import das libraries """

import numpy as np


""" Função e respetiva derivada  """

def g(x):
    g=np.log(x)+(1/x**2)-1
    return g

def dg(x):
    dg=(1/x)-(2/x**3)
    return dg

""" Métodos para determinar a raiz da função """

#Método da bissecção 
def bisec(a, b, k_max, eps_1, eps_2):
    k = 1
    c = (1/2)*(a+b)
    
    while k < 5:
        k += 1
        c = (1/2)*(a+b)
        if abs(g(c)) < eps_1 and b-a < eps_2:
            print(f"Converge em {k} iterações.")
            return c
        
        if g(a)*g(c) < 0:
            b = c
        else:
            a = c       
    return c

#Método de Newton 
def newton(g, dg, c, eps_1, eps_2, k_max):
    x = c
    k = 5
    while k < k_max:
        x_prev = x
        x = x - g(x) / dg(x)
        if abs(g(x)) < eps_1 and abs(x - x_prev) < eps_2:
            print(f"Converge em {k} iterações.")
            return x
        k += 1
    print(f"Falhou em convergir em {k_max} iterações.")
    return x


""" Introdução dos parametros """

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
k_max = int(input("Digite o número máximo de iterações: "))
eps_1 = float(input("Digite o valor de eps_1: "))
eps_2 = float(input("Digite o valor de eps_2: "))

result =  newton(g, dg, bisec(a, b, k_max, eps_1, eps_2), eps_1, eps_2, k_max)
print(f"A raiz da função é: {result}")