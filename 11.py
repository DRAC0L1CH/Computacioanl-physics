import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import t

# Define a função para ajuste linear
def linear_function(x, m, b):
    return m * x + b

# Função para obter os dados do URL
def get_data(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    return lines

# Função para ler os dados e criar o DataFrame
def read_data(lines):
    data = np.genfromtxt(lines[2:], skip_header=1)
    df = pd.DataFrame(data, columns=lines[1].split())
    return df

# Função para exibir as variáveis disponíveis
def display_variables(variable_names):
    print("Available Variables:")
    for i, var in enumerate(variable_names):
        print(f"{i + 1}: {var}")

# Função para realizar o ajuste de curva e retornar os parâmetros
def perform_curve_fit(x, y):
    popt, pcov = curve_fit(linear_function, x, y)
    return popt, pcov

# Função para calcular o coeficiente de correlação
def calculate_correlation_coefficient(x, y, popt):
    residuals = y - linear_function(x, *popt)
    ss_residuals = np.sum(residuals**2)
    ss_total = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_residuals / ss_total)
    correlation_coefficient = np.sqrt(r_squared)
    return correlation_coefficient, r_squared, ss_residuals

# Função para testar a hipótese de correlação
def test_correlation(correlation_coefficient, r_squared, n, alpha):
    t_critical = np.abs(t.ppf(alpha / 2, n - 2))
    threshold = t_critical * np.sqrt((1 - r_squared) / (n - 2))
    if correlation_coefficient > threshold:
        return True
    else:
        return False

# Função para calcular o erro do fator de inclinação
def calculate_slope_error(m_err, t_critical, ss_residuals, n, x):
    m_err *= t_critical * np.sqrt((ss_residuals / (n - 2)) / np.sum((x - np.mean(x))**2))
    return m_err

# Função para plotar os dados e a linha ajustada
def plot_graph(x, y, x_col_name, y_col_name, popt):
    plt.scatter(x, y, label='Data')
    plt.plot(x, linear_function(x, *popt), color='red', label='Fitted Line')
    plt.xlabel(x_col_name)
    plt.ylabel(y_col_name)
    plt.legend()

# Função para salvar a figura do gráfico
def save_figure():
    plt.savefig('figure.png', dpi=600)

# Função para salvar os valores x e y em um arquivo de dados
def save_data(x, y, x_col_name, y_col_name):
    output_data = np.column_stack((x, y))
    np.savetxt('data.dat', output_data, delimiter='\t', header=f"{x_col_name}\t{y_col_name}", comments='', fmt='%.8f')

# URL do arquivo de dados
url = 'https://trixi.coimbra.lip.pt/data/fc/fc11/courteau99.dat'

# Obter os dados do URL
lines = get_data(url)

# Ler os dados e criar o DataFrame
df = read_data(lines)

# Exibir as variáveis disponíveis
variable_names = lines[0].split()
display_variables(variable_names)

# Obter as variáveis escolhidas pelo usuário
print("Recomended x variable 'vlg' and y varianle 'L_B'")
x_col_name = input("Enter the name of the x-variable: ")
y_col_name = input("Enter the name of the y-variable: ")

# Encontrar os índices das colunas das variáveis escolhidas
x_col_index = variable_names.index(x_col_name)
y_col_index = variable_names.index(y_col_name)

# Extrair as colunas selecionadas
x = df.iloc[:, x_col_index].values
y = df.iloc[:, y_col_index].values

# Remover linhas com valores inválidos
mask = ~np.isnan(x) & ~np.isnan(y) & np.isfinite(x) & np.isfinite(y)
x = x[mask]
y = y[mask]

# Realizar o ajuste de curva
popt, pcov = perform_curve_fit(x, y)

# Extrair os parâmetros do ajuste
m, b = popt
m_err = np.sqrt(pcov[0, 0])

# Calcular o coeficiente de correlação
correlation_coefficient, r_squared, ss_residuals = calculate_correlation_coefficient(x, y, popt)
print(f"Correlation coefficient: {correlation_coefficient:.2f}")

# Testar a hipótese de correlação (com nível de confiança de 95%)
alpha = 0.05
n = len(x)
if test_correlation(correlation_coefficient, r_squared, n, alpha):
    print("The correlation is statistically significant at a 95% confidence level.")
else:
    print("The correlation is not statistically significant at a 95% confidence level.")

# Calcular o erro do fator de inclinação (com nível de confiança de 95%)
t_critical = np.abs(t.ppf(alpha / 2, n - 2))
m_err = calculate_slope_error(m_err, t_critical, ss_residuals, n, x)
print(f"Error of the slope factor (with 95% confidence level): {m_err:.2f}")

# Plotar os dados e a linha ajustada
plot_graph(x, y, x_col_name, y_col_name, popt)

# Salvar a figura do gráfico
save_figure()

# Salvar os valores x e y em um arquivo de dados
save_data(x, y, x_col_name, y_col_name)