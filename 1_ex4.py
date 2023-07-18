def binomial_coeff(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0 or k > n:
        return None
    
    # Compute using the smaller value of (n-k)
    if k > n-k:
        k = n-k
    
    # Compute the binomial coefficient using the formula
    res = 1
    for i in range(1, k+1):
        res = res * (n - (k - i)) // i
    
    return res

def binom(n, m):
    """
    Computes the probability of obtaining m heads in n coin tosses, where the probability of heads is 1/2.
    """
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0 or m > n:
        return None
    
    # Compute the probability using the binomial coefficient function
    coeff = binomial_coeff(n, m)
    p = coeff * (1/2)**n
    
    return p


n = int(input("Enter the number of coin tosses: "))
m = int(input("Enter the number of heads: "))

prob = binom(n, m)

print("The probability of obtaining", m, "heads in", n, "coin tosses is", prob)