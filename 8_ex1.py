import numpy as np
import matplotlib.pyplot as plt

def three_point_rule(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def five_point_rule(f, x, h):
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)

def three_point_rule_second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def five_point_rule_second_derivative(f, x, h):
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * (h ** 2))

f = lambda x: np.exp(x)
x = np.linspace(0, 12, num=1000)
y = f(x)
dydx_3 = three_point_rule(f, x, 0.001)
dydx_5 = five_point_rule(f, x, 0.001)
d2ydx2_3 = three_point_rule_second_derivative(f, x, 0.001)
d2ydx2_5 = five_point_rule_second_derivative(f, x, 0.001)

plt.plot(x, y, label='f(x)')
plt.plot(x, dydx_3, label="f'(x) (3-point rule)")
plt.plot(x, dydx_5, label="f'(x) (5-point rule)")
plt.plot(x, d2ydx2_3, label="f''(x) (3-point rule)")
plt.plot(x, d2ydx2_5, label="f''(x) (5-point rule)")
plt.legend()
plt.show()