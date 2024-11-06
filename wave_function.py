import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0  # Reduced Planck's constant
m = 1.0     # Mass of the particle
sigma_x = 1.0  # Initial width of the wave packet
k0 = 5.0      # Central wave number
t_max = 2.0   # Maximum time to evolve
dt = 0.01     # Time step

# Spatial grid
x_min = -10.0
x_max = 10.0
dx = 0.1
x = np.arange(x_min, x_max, dx)

# Initial Gaussian wave packet in x-space
def psi_x_0(x):
    return (1/(2*np.pi*sigma_x**2)**0.25) * np.exp(-x**2/(4*sigma_x**2)) * np.exp(1j * k0 * x)

# Fourier transform of the initial wave packet
def phi_k_0(k):
    return (sigma_x/np.pi**0.5)**0.5 * np.exp(-sigma_x**2 * (k - k0)**2 / 2)

# Time evolution factor in k-space
def time_evolution_factor(k, t):
    return np.exp(-1j * hbar * k**2 * t / (2 * m))

# Wave packet in x-space at time t
def psi_x_t(x, t):
    k = np.fft.fftfreq(x.size, d=dx) * 2 * np.pi
    phi_k_t = phi_k_0(k) * time_evolution_factor(k, t)
    psi_x_t = np.fft.ifft(phi_k_t) * x.size**0.5
    return psi_x_t

# Time evolution and plotting
times = np.arange(0, t_max, dt)
for t in times:
    psi_t = psi_x_t(x, t)
    plt.plot(x, np.abs(psi_t)**2, label=f't={t:.2f}')
    
plt.xlabel('x')
plt.ylabel('|Psi(x, t)|^2')
plt.title('Time Evolution of a Gaussian Wave Packet')
plt.legend()
plt.show()
