import numpy as np 
import time


def monte_carlo(f, a, b, n):
    x = np.random.uniform(low=a, high=b, size=n)
    fx = f(x)
    s = (b - a) * np.mean(fx)
    return s


def f(t):
    return  10*np.exp(-t)*np.sin(2*np.pi*t)


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
b = 1
valor_exato = 0.98120

n = int(input("Digite o número de iterações: "))

start_time = time.time()
result_mc = monte_carlo(f, a, b, n)
mc_time = time.time() - start_time

start_time = time.time()
result_simpson = simpson(f, a, b, n)
simpson_time = time.time() - start_time

print(f"Integral pelo método de Monte Carlo: {result_mc:.5f}, tempo: {mc_time:.5f}s")
print(f"Integral pelo método de Simpson: {result_simpson:.5f}, tempo: {simpson_time:.5f}s")
print(f"Valor exato: {valor_exato:.5f}")

erro_mc = abs(result_mc - valor_exato)
erro_simpson = abs(result_simpson - valor_exato)
print(f"Erro do método de Monte Carlo: {erro_mc:.5f}")
print(f"Erro do método de Simpson: {erro_simpson:.5f}")
