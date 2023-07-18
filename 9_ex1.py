import numpy as np
import matplotlib.pyplot as plt

def euler(h):
    n = int((2 - 0)/h) + 1
    x = np.linspace(0, 2, n)
    y = np.zeros(n)
    y[0] = 1
    for i in range(n-1):
        y[i+1] = y[i] + h*(y[i]*x[i]**2 - y[i])
    return x, y

# Analytical solution
x = np.linspace(0, 2, 200)
y_analytical = np.exp((x**3)/3 - x)

# Numerical approximations
x1, y1 = euler(0.01)
x2, y2 = euler(0.0001)

plt.plot(x, y_analytical, label='Analytical', color='r')
plt.plot(x1, y1, label='Euler h=0.01', color='g')
plt.plot(x2, y2, label='Euler h=0.0001', color='b',alpha=0.5)
plt.legend()
plt.title('Comparison of Analytical Solution and Numerical Approximations\n (0 <= x <= 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(color='grey', linestyle='--')
plt.savefig('plot.png', dpi=700)
plt.show()


