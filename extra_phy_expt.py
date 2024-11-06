import numpy as np
import matplotlib.pyplot as plt

# Define constants and parameters
h = 6.626e-34  # Planck's constant in Js
m = 9.109e-31  # Mass of an electron in kg
L = 1e-9       # Length of the box in meters

# Function to calculate energy levels
def energy_level(n):
 return (n**2 * h**2) / (8 * m * L**2)

# Function to calculate wave function
def wave_function(n, x):
 return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def prob(n,x):
    return wave_function(n,x)**2

# Create arrays for positions and quantum numbers
x = np.linspace(0, L, 1000)
n_values = [1, 2, 3]

for i in n_values:
    print(energy_level(i))
# Plot wave functions
plt.figure(figsize=(10, 8))
for n in n_values:
 plt.plot(x, wave_function(n, x), label=f'n={n}')
plt.title('Wave Functions of a Quantum Particle in a 1D Box')
plt.xlabel('Position (m)')
plt.ylabel('Wave Function')
plt.legend()
plt.grid(True)


# Plot wave functions
plt.figure(figsize=(10, 8))
for n in n_values:
 plt.plot(x, prob(n, x), label=f'n={n}')
plt.title('Wave Functions of a Quantum Particle in a 1D Box')
plt.xlabel('Position (m)')
plt.ylabel('Wave Function')
plt.legend()
plt.grid(True)
plt.show()
