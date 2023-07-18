""" Função e respetiva derivada  """

def f(x):
    f=25*x**(4)-x**(2)/2-2
    return f

def df(x):
    df=100*x**(3)-x
    return df


""" Métodos para determinar a raiz da função """

#Método da bissecção 
def bisec(a, b, k_max, eps_1, eps_2):
    k = 1
    c = (1/2)*(a+b)
    
    while k < k_max:
        k += 1
        c = (1/2)*(a+b)
        
        if abs(f(c)) < eps_1 and b-a < eps_2:
            print(f"Converge em {k} iterações.")
            return c
        
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        
    print("Não foi possível encontrar a raiz após", k_max, "iterações.")
    return c


#Método da Secante 
def sec(a, b, k_max, eps_1, eps_2):
    k = 1 
    c = a + f(a)*((a-b)/(f(b)-f(a)))
    while k < k_max:
        a = b
        b = c
        c = a + f(a)*((a-b)/(f(b)-f(a)))
        if abs(f(c)) < eps_1 and b-a < eps_2:
            print(f"Converge em {k} iterações.")
            return c
        k += 1
    if k == k_max:
        print("Não foi possível encontrar a raiz após", k_max, "iterações.")
    else:
        print("A raiz é:", c)
    
    return c

#Método de Newton 
def newton(f, df, x0, eps_1, eps_2, k_max):
    x = x0
    k = 1
    while k < k_max:
        x_prev = x
        x = x - f(x) / df(x)
        if abs(f(x)) < eps_1 and abs(x - x_prev) < eps_2:
            print(f"Converge em {k} iterações.")
            return x
        k += 1
    print(f"Falhou em convergir em {k_max} iterações.")
    return x


"""" Escolha do Método Pretendido  """

method = input("Qual o método que deseja utilizar?\n1. Bisseção \n2. Secante \n3. Newton's \nDigite o número correspondente: ")

while method not in ['1', '2', '3']:
    method = input("Método inválido. Tente novamente.\nQual o método que deseja utilizar?\n1. Bisection method\n2. Secant method\n3. Newton's method\nDigite o número correspondente: ")

if method == '1':
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    k_max = int(input("Digite o número máximo de iterações: "))
    eps_1 = float(input("Digite o valor de eps_1: "))
    eps_2 = float(input("Digite o valor de eps_2: "))

    
    result = bisec(a, b, k_max, eps_1, eps_2)
    print(f"A raiz da função é: {result}")

elif method == '2':
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    k_max = int(input("Digite o número máximo de iterações: "))
    eps_1 = float(input("Digite o valor de eps_1: "))
    eps_2 = float(input("Digite o valor de eps_2: "))


    result = sec(a, b, k_max, eps_1, eps_2)
    print(f"A raiz da função é: {result}")

else:
    x0 = float(input("Digite o valor de x0: "))
    k_max = int(input("Digite o número máximo de iterações: "))
    eps_1 = float(input("Digite o valor de eps_1: "))
    eps_2 = float(input("Digite o valor de eps_2: "))


    result =  newton(f, df, x0, eps_1, eps_2, k_max)
    print(f"A raiz da função é: {result}")
