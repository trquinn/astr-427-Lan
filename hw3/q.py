import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi

def bisection_method(func, a, b, tol=1e-10, max_iter=1000):
    if func(a) * func(b) > 0:
        raise ValueError("Function has the same sign at the endpoints.")
    errors = []
    for _ in range(max_iter):
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tol:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        true_root = np.sqrt(2)
        errors.append(abs(c - true_root))
    return c, errors

def newton_raphson_method(func, deriv, x0, tol=1e-10, max_iter=1000):
    errors = []
    for _ in range(max_iter):
        fx = func(x0)
        dfx = deriv(x0)
        if dfx == 0:
            raise ValueError("Derivative zero. No solution found.")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            break
        x0 = x1
        true_root = np.sqrt(2)
        errors.append(abs(x0 - true_root))
    return x0, errors

# Equations and derivatives
def equation_1(x, a=2.0):
    return x**2 - a

def derivative_1(x):
    return 2*x

def kepler_equation(E, M=1.5, e=0.5):
    return E - e * np.sin(E) - M

def derivative_kepler(E, e=0.5):
    return 1 - e * np.cos(E)

# Solving the equation x^2 = 2 using both methods
bisect_root, bisect_errors = bisection_method(equation_1, 0, 2)
newton_root, newton_errors = newton_raphson_method(equation_1, derivative_1, 1.5)

print("Bisection method root: ", bisect_root)
print("Newton-Raphson method root: ", newton_root)

# Plotting the errors
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.semilogy(bisect_errors, label='Bisection Method', marker='o')
plt.semilogy(newton_errors, label='Newton-Raphson Method', marker='x')
plt.title('Convergence for $x^2 = 2$')
plt.xlabel('Iteration Number')
plt.ylabel('Error (log scale)')
plt.legend()

# Kepler's equation for M = 1.5 and e = 0.5
E0 = 0.5  # Initial guess close to 0 but not zero
kepler_bisect_root, kepler_bisect_errors = bisection_method(lambda E: kepler_equation(E, 1.5, 0.5), 0, 2*pi)
kepler_newton_root, kepler_newton_errors = newton_raphson_method(lambda E: kepler_equation(E, 1.5, 0.5),
                                                                lambda E: derivative_kepler(E, 0.5), E0)

print("Kepler (e=0.5) Bisection method root: ", kepler_bisect_root)
print("Kepler (e=0.5) Newton-Raphson method root: ", kepler_newton_root)

plt.subplot(1, 2, 2)
plt.semilogy(kepler_bisect_errors, label='Bisection Method (Kepler e=0.5)', marker='o')
plt.semilogy(kepler_newton_errors, label='Newton-Raphson Method (Kepler e=0.5)', marker='x')
plt.title('Convergence for Kepler\'s Equation ($e = 0.5$)')
plt.xlabel('Iteration Number')
plt.ylabel('Error (log scale)')
plt.legend()

plt.tight_layout()
plt.show()
