import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, y0, t):
    """ Euler's method """
    y = np.array(y0)
    history = [y0]
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        y += dt * f(y, t[i-1])
        history.append(y.copy())
    return np.array(history)


def runge_kutta_4(f, y0, t):
    """ Fourth-order Runge-Kutta method """
    y = np.array(y0)
    history = [y0]
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        k1 = f(y, t[i-1])
        k2 = f(y + 0.5 * dt * k1, t[i-1] + 0.5 * dt)
        k3 = f(y + 0.5 * dt * k2, t[i-1] + 0.5 * dt)
        k4 = f(y + dt * k3, t[i])
        y += dt * (k1 + 2*k2 + 2*k3 + k4) / 6
        history.append(y.copy())
    return np.array(history)


# TRQ: In leapforg you need to pull out "x" and "v" from the y array
# so they can be treated separately.  E.g. for a 1 DOF system, x = y[0]
# and v = y[1]
def leapfrog_method(f, y0, t):
    """ Leapfrog method for second-order differential equations """
    y = np.array(y0)
    history = [y0]
    dt = t[1] - t[0]  # Assume uniform spacing
    v = f(y, t[0]) * dt / 2  # Initial half step velocity
    for i in range(1, len(t)):
        y += v * dt
        v += f(y, t[i]) * dt
        history.append(y.copy())
        
    # TRQ: Closing 1/2 step is missing.
    return np.array(history)

# Example usage for a system of coupled differential equations, dy/dt = f(y, t)


def f(y, t):
    # Example: Simple harmonic oscillator (second-order, converted to first-order system)
    # Let y = [x, v], then dy/dt = [v, -k*x] where k is the spring constant
    k = 1.0
    return np.array([y[1], -k * y[0]])


# Time steps
t = np.linspace(0, 10, 100)  # From 0 to 10 seconds, 100 steps
y0 = [1.0, 0.0]  # Initial conditions: x = 1.0, v = 0.0

# Solve using the different methods
euler_sol = euler_method(f, y0, t)
rk4_sol = runge_kutta_4(f, y0, t)
leapfrog_sol = leapfrog_method(f, y0, t)

# Q2

# Time intervals and step sizes
step_sizes = [1, 0.3, 0.1, 0.03, 0.01]
t_max = 30
errors = {'Euler': [], 'RK4': [], 'Leapfrog': []}

# Initial conditions
y0 = [1.0, 0.0]

# Solve and plot errors
for step in step_sizes:
    # TRQ: the "+ step" is to be sure the last point is included
    # roundoff error included an extra point, so I adjusted to 0.5*step.
    t = np.arange(0, t_max + 0.5*step, step)
    exact = np.cos(t)

    euler_sol = euler_method(f, y0, t)
    rk4_sol = runge_kutta_4(f, y0, t)
    leapfrog_sol = leapfrog_method(f, y0, t)

    # Calculate errors at t = 30
    errors['Euler'].append(np.log(np.abs(euler_sol[-1, 0] - np.cos(30))))
    errors['RK4'].append(np.log(np.abs(rk4_sol[-1, 0] - np.cos(30))))
    errors['Leapfrog'].append(np.log(np.abs(leapfrog_sol[-1, 0] - np.cos(30))))

# Plotting errors
plt.figure(figsize=(10, 6))
plt.plot(np.log(step_sizes), errors['Euler'], 'o-', label='Euler')
plt.plot(np.log(step_sizes), errors['RK4'], 's-', label='RK4')
# TRQ: commented this out so I could see the other lines.
# plt.plot(np.log(step_sizes), errors['Leapfrog'], '^-', label='Leapfrog')
plt.show()
