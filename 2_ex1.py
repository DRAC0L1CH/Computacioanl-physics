def f(x):
    f = 25 * x ** 4 - x ** 2 / 2 - 2
    return f

def df(x):
    df = 100 * x ** 3 - x
    return df

def bisec(a, b, k_max, eps_1, eps_2):
    k = 1
    c = (a + b) / 2
    
    while k <= k_max:
        print(f"Iteration {k}: a={a}, b={b}, c={c}, f(c)={f(c)}")
        
        if abs(f(c)) < eps_1 and b - a < eps_2:
            print(f"Converged after {k} iterations.")
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c = (a + b) / 2
        k += 1
    
    print("Failed to find the root after", k_max, "iterations.")
    return c

def sec(a, b, k_max, eps_1, eps_2):
    k = 1
    c = a + f(a) * ((a - b) / (f(b) - f(a)))
    
    while k <= k_max:
        print(f"Iteration {k}: a={a}, b={b}, c={c}, f(c)={f(c)}")
        
        if abs(f(c)) < eps_1 and b - a < eps_2:
            print(f"Converged after {k} iterations.")
            return c
        
        a = b
        b = c
        c = a + f(a) * ((a - b) / (f(b) - f(a)))
        k += 1
    
    print("Failed to find the root after", k_max, "iterations.")
    return c

def newton(f, df, x0, eps_1, eps_2, k_max):
    x = x0
    k = 1
    
    while k <= k_max:
        print(f"Iteration {k}: x={x}, f(x)={f(x)}")
        
        x_prev = x
        x = x - f(x) / df(x)
        
        if abs(f(x)) < eps_1 and abs(x - x_prev) < eps_2:
            print(f"Converged after {k} iterations.")
            return x
        
        k += 1
    
    print(f"Failed to converge after {k_max} iterations.")
    return x


method = input("Which method do you want to use?\n1. Bisection\n2. Secant\n3. Newton\nEnter the corresponding number: ")

while method not in ['1', '2', '3']:
    method = input("Invalid method. Try again.\nWhich method do you want to use?\n1. Bisection\n2. Secant\n3. Newton\nEnter the corresponding number: ")

if method == '1':
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    k_max = int(input("Enter the maximum number of iterations: "))
    eps_1 = float(input("Enter the value of eps_1: "))
    eps_2 = float(input("Enter the value of eps_2: "))
    
    result = bisec(a, b, k_max, eps_1, eps_2)
    print(f"The root of the function is: {result}")

elif method == '2':
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    k_max = int(input("Enter the maximum number of iterations: "))
    eps_1 = float(input("Enter the value of eps_1: "))
    eps_2 = float(input("Enter the value of eps_2: "))
    
    result = sec(a, b, k_max, eps_1, eps_2)
    print(f"The root of the function is: {result}")

else:
    x0 = float(input("Enter the value of x0: "))
    k_max = int(input("Enter the maximum number of iterations: "))
    eps_1 = float(input("Enter the value of eps_1: "))
    eps_2 = float(input("Enter the value of eps_2: "))
    
    result = newton(f, df, x0, eps_1, eps_2, k_max)
    print(f"The root of the function is: {result}")
