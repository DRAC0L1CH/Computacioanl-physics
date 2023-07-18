import numpy as np
import matplotlib.pyplot as plt

m = 50.0 # mass (kg)
c = 2.0e4 # elasticity constant (N/m)
b_values = [5000, 2500, 1000, 500, 100, 50] # damping constant (kg/s)

dt = float(input("Enter the iteration size (s): ")) # time step (s)
t = np.arange(0, 1+dt, dt) # time array
z0 = 0.1 # initial displacement (m)
v0 = 0 # initial velocity (m/s)

for b in b_values:
    z = np.zeros_like(t)
    v = np.zeros_like(t)
    z[0] = z0
    v[0] = v0
    for i in range(1, len(t)):
        z[i] = z[i-1] + v[i-1]*dt
        v[i] = v[i-1] + (-b/m*v[i-1] - c/m*z[i-1])*dt
    plt.plot(t, z, label=f"b={b}")

plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.show()