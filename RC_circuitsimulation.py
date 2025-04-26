import numpy as np
from matplotlib import pyplot as plt

V0 = 50    # Initial voltage in Volts
R = 10000  # Resistance in Ohms
C = 400e-6 # Capacitance in Farads
tau = R * C # Time constant

# Time points
t = np.linspace(0, 5*tau, 500)

# Voltage across capacitor
Vc = V0 * np.exp(-t/tau)

# Plot
plt.figure(figsize=(8,5))
plt.plot(t, Vc, label=f'$V_0$={V0}V, R={R}$\Omega$, C={C}F')
plt.title('Capacitor Discharge in RC Circuit')
plt.xlabel('Time (s)')
plt.ylabel('Voltage across Capacitor (V)')
plt.grid(True)
plt.legend()
plt.show()