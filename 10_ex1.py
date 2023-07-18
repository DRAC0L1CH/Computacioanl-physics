import numpy as np
import matplotlib.pyplot as plt

def gaussian_elimination(A, b, pivoting=True):
    n = A.shape[0]
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)
    for i in range(n-1):
        if pivoting:
            pivot_row = np.argmax(np.abs(Ab[i:, i])) + i
            Ab[[i, pivot_row]] = Ab[[pivot_row, i]]
        pivot = Ab[i, i]
        if pivot == 0:
            raise ValueError('Zero pivot encountered, unable to proceed with elimination.')
        Ab[i, :] /= pivot
        for j in range(i+1, n):
            multiplier = Ab[j, i]
            Ab[j, :] -= multiplier * Ab[i, :]
    if Ab[-1, -2] == 0:
        raise ValueError('Zero pivot encountered in the last row, unable to solve the system uniquely.')
    x = np.zeros(n)
    x[-1] = Ab[-1, -1] / Ab[-1, -2]
    for i in range(n-2, -1, -1):
        x[i] = (Ab[i, -1] - Ab[i, i+1:n] @ x[i+1:]) / Ab[i, i]
    return x

def polynomial_approximation(x_data, y_data, degree, pivoting=True):
    n = degree + 1
    X = np.zeros((n,n))
    Y = np.zeros(n)
    for i in range(n):
        Y[i] = np.sum(y_data * x_data**i)
        for j in range(n):
            X[i,j] = np.sum(x_data**(i+j))
    coefficients = gaussian_elimination(X,Y,pivoting)
    return coefficients

# Example data
x_data = np.array([1, 2, 4, 8, 6, 5, 8, 9, 7])
y_data = np.array([2, 3, 4, 7, 6, 5, 8, 8, 6])

# Degree of polynomial
degree = 1

# Compute polynomial approximation
pivoting = input('Do you want to use pivoting? (y/n): ').lower() == 'y'
coefficients = polynomial_approximation(x_data,y_data,degree,pivoting)

# Plot data points and approximation function
x_range = np.linspace(np.min(x_data),np.max(x_data),100)
y_range = np.polyval(coefficients[::-1],x_range)
plt.plot(x_data,y_data,'ro',label='Data')
plt.plot(x_range,y_range,label='Approximation',linestyle='--',alpha=0.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
plt.savefig('polynomial_approximation0.png')