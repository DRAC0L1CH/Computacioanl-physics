import numpy as np
import matplotlib.pyplot as plt

l1 = 0.9  # decay constant for N1
l2 = 0.3  # decay constant for N2
l3 = 0.0  # decay constant for N3

N1_0 = 100000  # initial number of N1 nuclei
N2_0 = 0  # initial number of N2 nuclei
N3_0 = 0  # initial number of N3 nuclei

t_max = 3.0  # maximum time for the simulation
dt_values = [1.0, 0.1, 0.01]  # time intervals for the simulation

fig, axs = plt.subplots(3, 1, figsize=(8, 12))  # create subplots

for i, dt in enumerate(dt_values):
    t = np.arange(0, t_max+dt, dt)  # time array for the simulation

    N1 = np.zeros(len(t))
    N2 = np.zeros(len(t))
    N3 = np.zeros(len(t))

    N1[0] = N1_0
    N2[0] = N2_0
    N3[0] = N3_0

    for j in range(1, len(t)):
        decay1 = np.random.rand(N1[j-1].astype(int)) < l1*dt
        decay2 = np.random.rand(N2[j-1].astype(int)) < l2*dt

        N1[j] = N1[j-1] - np.sum(decay1)
        N2[j] = N2[j-1] + np.sum(decay1) - np.sum(decay2)
        N3[j] = N3[j-1] + np.sum(decay2)

    axs[i].plot(t, N1, label='N1 λ1 = 0.9/s')
    axs[i].plot(t, N2, label='N2 λ2 = 0.3/s')
    axs[i].plot(t, N3, label='N3 λ3 = 0')
    axs[i].set_xlabel('t [s]')
    axs[i].set_ylabel('n (t)')
    axs[i].set_title(f'Decay Δt={dt}s')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.savefig('decay3.png')
