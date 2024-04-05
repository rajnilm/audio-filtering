import numpy as np
import matplotlib.pyplot as plt

# Given values of r(i), p(i), and k(i)
r_values = [0.0590691 -0.14376742j, 
            0.0590783 +0.14379876j, 
            -0.05908098+0.02467098j, 
            -0.05907123-0.02467015j]

p_values = [0.8879774 +0.04375594j, 
            0.8869765 -0.04376678j, 
            0.94552098+0.11263232j, 
            0.94552062-0.11263232j]

k_values = [2.19e-5, 0, 0, 0]

# Time indices
n_values = np.arange(31)  # n values up to 30

# Compute h(n)
hn_values = np.zeros_like(n_values, dtype=np.complex128)
for n in n_values:
    for i in range(len(r_values)):
        hn_values[n] += r_values[i] * (p_values[i] ** n)
    for j in range(len(k_values)):
        if n - j >= 0:
            hn_values[n] += k_values[j]

# Plot
plt.stem(n_values, np.abs(hn_values))
plt.xlabel('$n$')
plt.ylabel('$|h(n)|$')
plt.title('Magnitude of $h(n)$')
plt.grid(True)
plt.show()
