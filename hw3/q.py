import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi
import time

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


# Q2
def kepler_solution(M_values, e, method='bisection', max_iter=1000):
    results = []
    start_time = time.time()

    if method == 'bisection':
        for M in M_values:
            root, _ = bisection_method(lambda E: kepler_equation(E, M, e), 0, 2*pi, max_iter=max_iter)
            results.append(root)
    elif method == 'newton':
        E0 = 0.5  # Initial guess
        for M in M_values:
            root, _ = newton_raphson_method(lambda E: kepler_equation(E, M, e),
                                            lambda E: derivative_kepler(E, e), E0, max_iter=max_iter)
            results.append(root)
            E0 = root  # Use last root as initial guess for next

    elapsed_time = time.time() - start_time
    return results, elapsed_time

# 10,000 equally spaced values of M between 0 and 2π
M_values = np.linspace(0, 2*pi, 10000)
e = 0.9

# Solve Kepler's equation using both methods
bisection_results, bisection_time = kepler_solution(M_values, e, method='bisection')
newton_results, newton_time = kepler_solution(M_values, e, method='newton')

print(f"Bisection method time: {bisection_time:.4f} seconds")
print(f"Newton-Raphson method time: {newton_time:.4f} seconds")

"""

The significant performance difference between the Bisection and Newton-Raphson methods in solving Kepler's equation for  𝑒 = 0.9
primarily stems from the faster convergence rate of the Newton-Raphson method. Each iteration of Newton-Raphson method generally
reduces the error more rapidly than the Bisection method, which halves the search interval irrespective of the function's behavior.
Additionally, by using the solution from one value of 𝑀 as the initial guess for the next, the Newton-Raphson method leverages
the continuity in the behavior of Kepler's equation to further speed up convergence. This approach minimizes the number of iterations
needed to achieve a solution, thus reducing the overall computation time substantially compared to the more methodical and
consistently paced Bisection method.
"""
