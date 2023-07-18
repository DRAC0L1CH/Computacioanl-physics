""" Import das libraries """ 

from math import sqrt


""" Definição das funções """

def f(x,y):
    return x-y

#derivada de f em funcao de x
def dfx(x):
    return 1

#derivada de f em funcao de y
def dfy(y):
    return -1

#funcao de gauss para determinar se são iguais ou diferentes  
def gauss(x,y,dx,dy):
    erro = sqrt((dfx(x)*dx)**2+(dfy(y)*dy)**2)
    print(f"x-y = {f(x,y):.4f}     +-      {erro:.4f}")
    if abs(f(x,y)) > erro:
        return "Os numeros sao diferentes"
    else:
        return "Os numeros sao iguais"

    
""" Input dos valores necessários """


x = float(input("Enter the value of x: "))
print("==========================")
y = float(input("Enter the value of y: "))
print("==========================")
dx = float(input("Enter the error in x: "))
print("==========================")
dy = float(input("Enter the error in y: "))
print("==========================")
print (gauss(x,y,dx,dy))