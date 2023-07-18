import numpy as np

# Define Newton method function
def newton(g, dydx_3, x0, eps_1, eps_2, k_max):
    x = x0
    k = 1
    while k < k_max:
        x_prev = x
        x = x - g(x) / dydx_3
        if abs(g(x)) < eps_1 and abs(x - x_prev) < eps_2 * abs(x):
            print(f"Converge em {k} iterações.")
            return x
        k += 1
    print(f"Falhou em convergir em {k_max} iterações.")
    return x

def three_point_rule(g, x, h):
    return (g(x + h) - g(x - h)) / (2 * h)

g = lambda x: np.log(x)+(1/x**2)-1
x = np.logspace(0, 12, num=1000)
y = g(x)

# Find best h value for the 3-point rule
x0 = float(input("Digite o valor de x0: "))
true_dydx = g(x0)
best_h_dydx_3 = 0
best_error_dydx_3 = np.inf
for k in range(1, 15):
    h = 10 ** (-k)
    dydx_3 = three_point_rule(g, x0, h)
    rel_error_dydx_3 = abs((dydx_3 - true_dydx) / true_dydx)
    if rel_error_dydx_3 < best_error_dydx_3:
        best_h_dydx_3 = h
        best_error_dydx_3 = rel_error_dydx_3

# Perform Newton method using the 3-point rule with best h value
dydx_3 = three_point_rule(g, x0, best_h_dydx_3)
k_max = int(input("Digite o número máximo de iterações: "))
eps_1 = float(input("Digite o valor de eps_1: "))
eps_2 = float(input("Digite o valor de eps_2: "))
result = newton(g, dydx_3, x0, eps_1, eps_2, k_max)
print(f"A raiz da função é: {result}")