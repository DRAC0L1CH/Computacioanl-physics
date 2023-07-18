import numpy as np
import matplotlib.pyplot as plt

N1 = 100000
N2 = 0
N3 = 0

dt = 0.1

l1 = 0.1
l2 = 0.3
l3 = 0

t = np.arange(0, 20 + dt, dt)

N1_array = np.zeros(len(t))
N2_array = np.zeros(len(t))
N3_array = np.zeros(len(t))


N1_array[0] = N1
N2_array[0] = N2
N3_array[0] = N3

for i in range(1, len(t)):
    # Determina pelo método de Monte Carlo para cada nucleo N1 e N2 se estes vão decair. 
    decay1 = np.random.rand(N1_array[i-1].astype(int)) < l1*dt
    decay2 = np.random.rand(N2_array[i-1].astype(int)) < l2*dt

    # Determina o número de nucleos N1, N2, N3 depois de cada intrevalo Δt.
    N1 = N1 - np.sum(decay1)
    N2 = N2 + np.sum(decay1) - np.sum(decay2)
    N3 = N3 + np.sum(decay2)

    # Armazena o número de núcleos N1, N2 e N3 numa matriz. 
    N1_array[i] = N1
    N2_array[i] = N2
    N3_array[i] = N3

# Graph the number of nuclei per time for the three nuclei in the same diagram for 0 ≤ t ≤ 100s and 0 ≤ t ≤ 20s.
plt.plot(t, N1_array, label='N1 λ1 = 0.1/s')
plt.plot(t, N2_array, label='N2 λ2 = 0.3/s')
plt.plot(t, N3_array, label='N3 λ3 = 0')
plt.xlabel('t [s]')
plt.ylabel('n (t)')
plt.title('Decaimento Δt=0.1')
plt.legend()
plt.grid(True)
plt.savefig('decay2.png')
