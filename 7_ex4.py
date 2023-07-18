import numpy as np
from numpy.lib._datasource import open as open_url

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

# load data from URL using numpy.lib._datasource.open()
url = "https://trixi.coimbra.lip.pt/data/fc/fc07/f07-p3a.npz"
with open_url(url, "rb") as file:
    npzfile = np.load(file)
    A = npzfile['A']
    b = npzfile['b']
    
print('Without pivoting(A):')
x = gaussian_elimination(A, b, False)
print('Solution: ', x)

# Check the result
residuals = A @ x - b
largest_error = np.max(np.abs(residuals))
sum_of_errors = np.sum(np.abs(residuals))
print('Largest absolute error: ', largest_error)
print('Sum of absolute errors: ', sum_of_errors)
print('------------------------------------------------------')


url2 = "https://trixi.coimbra.lip.pt/data/fc/fc07/f07-p3d.npz"
with open_url(url2, "rb") as file:
    npzfile = np.load(file)
    B = npzfile['A']
    d = npzfile['b']
    
 
print('Without pivoting(B): ')
x2 = gaussian_elimination(B, d, False)
print('Solution: ', x2)


# Check the result
residuals2 = B @ x2 - d
largest_error2 = np.max(np.abs(residuals2))
sum_of_errors2 = np.sum(np.abs(residuals2))
print('Largest absolute error: ', largest_error2)
print('Sum of absolute errors: ', sum_of_errors2)

print('=====================================================')

print('With pivoting (A):')
x = gaussian_elimination(A, b, True)
print('Solution: ', x)

# Check the result
residuals = A @ x - b
largest_error = np.max(np.abs(residuals))
sum_of_errors = np.sum(np.abs(residuals))
print('Largest absolute error: ', largest_error)
print('Sum of absolute errors: ', sum_of_errors)
print('------------------------------------------------------')


print('With pivoting (B): ')
x2 = gaussian_elimination(B, d, True)
print('Solution: ', x2)

# Check the result
residuals2 = B @ x2 - d
largest_error2 = np.max(np.abs(residuals2))
sum_of_errors2 = np.sum(np.abs(residuals2))
print('Largest absolute error: ', largest_error2)
print('Sum of absolute errors: ', sum_of_errors2)