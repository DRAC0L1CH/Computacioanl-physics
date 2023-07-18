import numpy as np
import matplotlib.pyplot as plt

# Set decay constants
lambda_N1_N2 = 0.5   # Decay constant for N1 → N2
lambda_N2_N4 = 0.1   # Decay constant for N2 → N4
lambda_N1_N3 = 0.4   # Decay constant for N1 → N3
lambda_N3_N4 = 0.1   # Decay constant for N3 → N4

# Set initial number of nuclei
N1_0 = 100000   # Initial number of N1 nuclei
N2_0 = 0       # Initial number of N2 nuclei
N3_0 = 0       # Initial number of N3 nuclei
N4_0 = 0       # Initial number of N4 nuclei

# Set time step and time array
dt = 0.01         # Time step (in seconds)
t = np.arange(0, 50, dt)    # Time array

# Set probability of decay for each time step
P_N1_N2 = 1 - np.exp(-lambda_N1_N2*dt)    # Probability of N1 → N2 decay
P_N2_N4 = 1 - np.exp(-lambda_N2_N4*dt)    # Probability of N2 → N4 decay
P_N1_N3 = 1 - np.exp(-lambda_N1_N3*dt)    # Probability of N1 → N3 decay
P_N3_N4 = 1 - np.exp(-lambda_N3_N4*dt)    # Probability of N3 → N4 decay

# Initialize arrays to store number of nuclei at each time step
N1 = np.zeros_like(t)
N2 = np.zeros_like(t)
N3 = np.zeros_like(t)
N4 = np.zeros_like(t)

# Set initial values
N1[0] = N1_0
N2[0] = N2_0
N3[0] = N3_0
N4[0] = N4_0

# Simulate decay process
for i in range(len(t)-1):
    # N1 → N2
    N1[i+1] = N1[i] - np.random.binomial(N1[i], P_N1_N2)
    N2[i+1] = N2[i] + np.random.binomial(N1[i], P_N1_N2) - np.random.binomial(N2[i], P_N2_N4)
    # N1 → N3
    N1[i+1] = N1[i+1] - np.random.binomial(N1[i+1], P_N1_N3)
    N3[i+1] = N3[i] + np.random.binomial(N1[i+1], P_N1_N3) - np.random.binomial(N3[i], P_N3_N4)
    # N2 → N4 and N3 → N4
    N4[i+1] = N4[i] + np.random.binomial(N2[i], P_N2_N4) + np.random.binomial(N3[i], P_N3_N4)


plt.grid(True)
plt.plot(t, N1, label='N1')
plt.plot(t, N2, label='N2')
plt.plot(t, N3, label='N3')
plt.plot(t, N4, label='N4')
plt.legend()
plt.xlabel('t [s]')
plt.ylabel('n (t)')
plt.title('Simulação de Cadeia de Decaimento')
plt.savefig('decay4.png')
