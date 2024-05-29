import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import logit, expit  # for the hyperbolic secant
# TRQ: I don't have a "rich" module.
# from rich import print

# Function to compute the hyperbolic secant
def sech(x):
    return 2 / (np.exp(x) + np.exp(-x))

# Stellar density model function
# TRQ: document arguments
def rho_star(z, rho_thin, rho_thick, h_thin, h_thick):
    return rho_thin * sech(z / h_thin)**2 + rho_thick * sech(z / h_thick)**2

# Function to compute the sum of squared residuals
# TRQ: document arguments
def sum_of_squares(params, z, rho_obs):
    rho_thin, rho_thick, h_thin, h_thick = params
    rho_model = rho_star(z, rho_thin, rho_thick, h_thin, h_thick)
    return np.sum((rho_obs - rho_model) ** 2)

# Load the data
data = pd.read_csv('./hw4/disk.csv', header=None, names=['z', 'rho_star'])
z_obs = data['z'].values
rho_obs = data['rho_star'].values

# Initial guesses for parameters
initial_params = [0.01, 0.01, 300, 800]  # Example: [rho_thin, rho_thick, h_thin, h_thick]

# Fit the model
result = minimize(sum_of_squares, initial_params, args=(z_obs, rho_obs), method='Powell')

# Output the results
if result.success:
    print("\nQ1: Optimal parameters found:")
    print(f"rho_thin = {result.x[0]}")
    print(f"rho_thick = {result.x[1]}")
    print(f"h_thin = {result.x[2]}")
    print(f"h_thick = {result.x[3]}")
else:
    print("Optimization failed:", result.message)





# Q2
# Modified to fit only the thin disk parameters with fixed thick disk properties
def rho_star_thin_only(z, rho_thin, h_thin, rho_thick=0.003, h_thick=800):
    return rho_thin * sech(z / h_thin)**2 + rho_thick * sech(z / h_thick)**2

# Function to compute the sum of squared residuals for thin disk only
def sum_of_squares_thin(params, z, rho_obs):
    rho_thin, h_thin = params
    rho_model = rho_star_thin_only(z, rho_thin, h_thin)
    return np.sum((rho_obs - rho_model) ** 2)

# Initial guesses for thin disk parameters only
initial_params_thin = [0.1, 300]  # Example: [rho_thin, h_thin]

# Fit the model for the thin disk only
result_thin = minimize(sum_of_squares_thin, initial_params_thin, args=(z_obs, rho_obs), method='Powell')

# Output the results for the thin disk
if result_thin.success:
    print("\nQ2: Optimal parameters found for the thin disk:")
    print(f"rho_thin = {result_thin.x[0]}")
    print(f"h_thin = {result_thin.x[1]}")
else:
    print("Optimization failed:", result_thin.message)




# Q3
# Known values used to generate the data
known_values = {
    "rho_thin": 0.004,  # in /pc^3
    "h_thin": 280,      # in pc
    "rho_thick": 0.003, # in /pc^3
    "h_thick": 800      # in pc
}

# Errors for the density values
error_margin = 0.0004

# TRQ: this function could use a lot more commenting as to what the argument is
# and what it does.
# Compare and comment on the results
def compare_parameters(optimized_params):
    print("\nQ3: Comparison with known values:")
    for param in optimized_params:
        estimated = optimized_params[param]
        known = known_values[param]
        discrepancy = abs(estimated - known)
        within_error = discrepancy <= error_margin

        print(f"{param}: Estimated = {estimated:.6f}, Known = {known:.6f}, Discrepancy = {discrepancy:.6f}")
        if within_error:
            print(f"The estimated {param} is within the acceptable error range.")
        else:
            print(f"The estimated {param} exceeds the acceptable error range.")

# Assuming you have the results from problem 1 or 2
optimized_params = {
    "rho_thin": result.x[0],
    "h_thin": result.x[2],
    "rho_thick": result.x[1],
    "h_thick": result.x[3]
}

compare_parameters(optimized_params)
