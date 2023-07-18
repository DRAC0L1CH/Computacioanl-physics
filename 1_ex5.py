def factorial(n):
    """
    Computes the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binom(n, m):
    """
    Computes the probability of obtaining m heads in n coin tosses, where the probability of heads is 1/2.
    """
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0 or m > n:
        return None
    else:
        return factorial(n) // (factorial(m) * factorial(n-m)) * 2**(-n)

n = int(input("Enter the number of coin tosses: "))

# Initialize the sum of probabilities to zero
total_prob = 0

# Iterate over all possible values of m and compute the probability for each value
for m in range(n+1):
    prob = binom(n, m)
    if prob is not None:
        print("The probability of obtaining", m, "heads in", n, "coin tosses is", prob)
        total_prob += prob
    else:
        print("Invalid input.")

# Print the sum of all probabilities
print("The sum of probabilities is", total_prob)