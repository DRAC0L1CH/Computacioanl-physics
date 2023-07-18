import numpy as np 
import time


def monte_carlo(f, a, b, n):
   
    subsets = np.arange(0,n+1,n/10)
    u = np.zeros(n)
    for i in range(10):
        start = int(subsets[i])
        end = int(subsets[i+1])
        u[start:end] = np.random.uniform(low=i/10,high=(i+1)/10,size=end-start)
    np.random.shuffle(u)
    u_func = f(a+(b-a)*u)
    s = ((b-a)/n)*u_func.sum()
    
    return s

def f(t):
    return  (10*np.exp(-t)*np.sin(2*np.pi*t))**2


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


a = 0
b = 0.5
valor_exato = 15.41260804810169

n = int(input("Digite o número de iterações: "))

start_time = time.time()
result3 = simpson(f,a,b,n)
simpson_time = time.time() - start_time
print(f"Integral pelo método de Simpson: {result3:.5f}, tempo: {simpson_time:.5f}s")

start_time = time.time()
result = monte_carlo(f, a, b, n)
monte_carlo_time = time.time() - start_time
print(f"Integral pelo método de Monte Carlo: {result:.5f}, tempo: {monte_carlo_time:.5f}s")
