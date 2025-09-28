#Bifurcation Diagram for the logistic map
import numpy as np
import matplotlib.pyplot as plt

# Parameters
lam_values = np.linspace(2.5, 4.0, 10000)  # X-axis: lambda (bifurcation parameter)
iterations = 1000                         # Total iterations per lambda
last = 100                                # Number of iterations to plot (after transients)

# Prepare figure
x = 1e-5 * np.ones_like(lam_values)       # Initial condition (small non-zero value)

plt.figure(figsize=(12, 7))
for i in range(iterations):
    x = lam_values * x * (1 - x)          # Logistic map equation
    if i >= (iterations - last):
        plt.plot(lam_values, x, ',k', alpha=0.25)  # tiny black dots

plt.title("Bifurcation Diagram of the Logistic Map")
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$x$')
plt.xlim(2.5, 4.0)
plt.ylim(0, 1)
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()