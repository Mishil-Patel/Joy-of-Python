import numpy as np
import matplotlib.pyplot as plt

# Define constants
L = 2.0  # Length of the potential well (in arbitrary units)

# Function to calculate wave function for a given energy level n
def wave_function(n, x):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

# Function to plot wave function and probability density
def plot_wave_function(n):
    x = np.linspace(0, L, 1000)
    psi_n = wave_function(n, x)
    P_n = psi_n ** 2  # Probability density

    # Plot the wave function
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, psi_n, label=f'Wave Function for n={n}')
    plt.axvline(x=0, color='red', linestyle='--', label='Well Boundary')
    plt.axvline(x=L, color='red', linestyle='--')
    plt.title(f'Wave Function for n={n}')
    plt.xlabel('Position (x)')
    plt.ylabel(r'$\psi_n(x)$')
    plt.grid(True)
    plt.legend()

    # Plot the probability density
    plt.subplot(1, 2, 2)
    plt.plot(x, P_n, label=f'Probability Density for n={n}', color='orange')
    plt.axvline(x=0, color='red', linestyle='--', label='Well Boundary')
    plt.axvline(x=L, color='red', linestyle='--')
    plt.title(f'Probability Density for n={n}')
    plt.xlabel('Position (x)')
    plt.ylabel(r'$|\psi_n(x)|^2$')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Interactive loop for user input
while True:
    try:
        n = int(input("Enter energy level number (n), or type 0 to exit: "))
        if n <= 0:
            print("Exiting the program.")
            break
        plot_wave_function(n)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
