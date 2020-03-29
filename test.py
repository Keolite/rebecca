#----------------------------------------------------------------
# Program 1: Numerical Integration and Plotting using python
#----------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
N = int(1e6)  # No. of points.
L = 500      # Range of x: from -L to L.
# Generate column vector with N x values ranging from -L to L.
(x, dx) = np.linspace(-L, L, num=N, retstep=True)
print("dx=", dx)  # What is dx?

# Alternative Trial functions:
# To select one, delete the comment character '#' at the beginning.
#  y = np.exp(-x**2/2000)                                       # Gaussian centered at x=0.
A = 3000
y = ((2*A*np.pi)**-0.5) * np.exp(-(x-100)**2/(2*A))
# Normed Gaussian at x=100.
# y = (-100-x**2)**-1                                         # Symmetric fcn, blows up at x=1.
# y = (np.cos(np.pi*x))**2                                    # Cosine fcn.
# y = np.exp(np.pi*x*1j)                                      # Complex exponential.
# y = np.sin(np.pi*x/L) * np.cos(np.pi*x/L)                   # Product of sinx times cosx.
# y = np.sin(np.pi*x/L) * np.sin(np.pi*x/L)                   # Product of sin(nx) times sin(mx).
# A = 100; y = np.sin(x*A) / (np.pi*x)                        # Rep. of delta fcn.
# A = 20; y = (np.sin(x*A)**2) / (np.pi*(A*x**2))             # Another rep. of delta fcn.

# Build your own function here!

# Observe: a function y(x) is numerically represented by a vector!
# Plot a vector/function.
plt.plot(np.real(x), np.real(y), '-')  # Plots vector y vs x.
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# Numerical Integration
I_trap = np.trapz(y) * dx  # Integration using trapezoidal rule.
print("I_trap=", I_trap)
