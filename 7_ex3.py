import numpy as np
from numpy.lib._datasource import open as open_url

def inverse(A):
    n = A.shape[0]
    A_inv = np.zeros((n, n))
    for i in range(n):
        b = np.zeros(n)
        b[i] = 1
        x = gaussian_elimination(A.copy(), b)
        A_inv[:, i] = x
    return A_inv

def gaussian_elimination(A, b):
    n = A.shape[0]
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)
    for i in range(n-1):
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
url = "https://trixi.coimbra.lip.pt/data/fc/fc07/f07-p1c.npz"
with open_url(url, "rb") as file:
    npzfile = np.load(file)
    A = npzfile['A']

A_inv = inverse(A)

print('Inverse of A: ')
print(A_inv)