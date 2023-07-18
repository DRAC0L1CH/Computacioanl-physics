def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def factorial2(n, m):
    if n >= m:
        s = n
        p = 1
        while s > m:
            p *= s
            s -= 1
        return p

def binom(n, m):
    P = factorial2(n, m) / (factorial(n - m) * (2 ** n))
    return P

print("Probabilidade de lançar 100,0000 moedas e obter 50,000 caras:", binom(100000, 50000))
print("Probabilidade de lançar 10,000 moedas e obter 5,000 caras:", binom(10000, 5000))