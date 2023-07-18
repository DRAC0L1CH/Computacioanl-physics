def binom(n, m):
    """
    Calcula a probabilidade de obter m "heads" em n lançamentos de moeda, onde a probabilidade de "heads" é 1/2.
    """
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0 or m > n:
        return None
    
    numerator = 1
    denominator = 1
    
    for i in range(m):
        numerator *= (n - i)
        denominator *= (i + 1)
    
    return numerator // denominator * 2**(-n)

n = int(input("Enter the number of coin tosses: "))
m = int(input("Enter the number of heads: "))

prob = binom(n, m)

if prob is not None:
    print("The probability of obtaining", m, "heads in", n, "coin tosses is", prob)
else:
    print("Invalid input.")