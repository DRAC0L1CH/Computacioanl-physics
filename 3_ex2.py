import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Access the Excel file from the URL
url = 'https://trixi.coimbra.lip.pt/data/fc/fc03/data-2019244037.xlsx'
df = pd.read_excel(url)

# Calcula o periodo expectável T = 2*pi*sqrt(L/g)
g = 9.81 # m/s^2
df['Expected Period'] = 2*np.pi*np.sqrt(df['Length']/g)

# Calcula o erro no periodo expectável
df['Error in Expected Period'] = np.sqrt((np.pi**2/g*np.sqrt(df['Length']))*df['dLength']**2)

# Define as funções
def f(x,y):
    return x-y

def dfx(x):
    return 1

def dfy(y):
    return -1

def gauss(x,y,dx,dy):
    erro = np.sqrt((dfx(x)*dx)**2+(dfy(y)*dy)**2)
    if abs(f(x,y)) > erro:
        return "no"
    else:
        return "yes"

# Aplica a função de gauss para criar uma nove coluna 'Equal?'
df['Equal?'] = df.apply(lambda row: gauss(row['Period'], row['Expected Period'], row['dPeriod'], row['Error in Expected Period']), axis=1)

# Define os parametros necessários para o plot
dx = df['dPeriod']
dy = df['Error in Expected Period']
x = df['Period']
y = df['Expected Period']

# Conta o número de "yes"
num_yes = df['Equal?'].value_counts()['yes']
print(f"Numero de potos pontos com períodos iguais: {num_yes}")

# Plot dos dados e o período expectável
plt.errorbar(df['Length'], df['Period'], yerr=df['dPeriod'], marker='o', linestyle='none')
plt.plot(df['Length'], df['Period'], 'o', label='Periodo observado')
plt.plot(df['Length'], df['Expected Period'], '-', label='Periodo Esperado')
plt.xlabel('Comprimento (m)')
plt.ylabel('Periodo (s)')
plt.title('Periodo em função do comprimento')
plt.legend()
plt.show()

# Guarda os dados atualizados num novo excel e json
filename_excel = "updated_data.xlsx"
filename_json = "updated_data.json"
df.to_excel(filename_excel, index=False)
df.to_json(filename_json, orient='records')
