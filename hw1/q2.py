import numpy as np

'''
Question 2: Roundoff Error

Numerically evaluate the expression (1−cos(x))/x2 in double precision 
for values of x around 10−7 and smaller. 
Explain the difference between the numerical results and the analytic limit 
as x → 0.
'''

def function(x):
    return (1.0 - np.cos(x)) / (x**2)


# Starting value and preparation for results
x_start = 10**(-5)
xs, ys = [], []

# Iterating to generate values of x and corresponding function evaluations
for i in range(20):
    xs.append(x_start)
    ys.append(function(x_start))
    x_start /= 2.0

# Printing results for analysis
for i in range(len(xs)):
    print(f'x: {xs[i]:.3E}\ty: {ys[i]:.3E}\t1-cos[x]: {1-np.cos(xs[i]):.3E}')

'''
Output:

x: 1.000E-05    y: 5.000E-01    1-cos[x]: 5.000E-11
x: 5.000E-06    y: 5.000E-01    1-cos[x]: 1.250E-11
x: 2.500E-06    y: 5.000E-01    1-cos[x]: 3.125E-12
x: 1.250E-06    y: 5.000E-01    1-cos[x]: 7.813E-13
x: 6.250E-07    y: 4.999E-01    1-cos[x]: 1.953E-13
x: 3.125E-07    y: 5.002E-01    1-cos[x]: 4.885E-14
x: 1.563E-07    y: 5.002E-01    1-cos[x]: 1.221E-14
x: 7.813E-08    y: 4.911E-01    1-cos[x]: 2.998E-15
x: 3.906E-08    y: 5.093E-01    1-cos[x]: 7.772E-16
x: 1.953E-08    y: 5.821E-01    1-cos[x]: 2.220E-16
x: 9.766E-09    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 4.883E-09    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 2.441E-09    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 1.221E-09    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 6.104E-10    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 3.052E-10    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 1.526E-10    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 7.629E-11    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 3.815E-11    y: 0.000E+00    1-cos[x]: 0.000E+00
x: 1.907E-11    y: 0.000E+00    1-cos[x]: 0.000E+00



Explanation:

The difference between the numerical results and the analytic limit as x → 0
arises primarily from the limitations of floating-point arithmetic in representing
very small numbers and performing operations on them. 

Analytically, the limit of this expression as x approaches 0 is 1/2, a result derived
from L'Hopital's rule. However, as x becomes very small (< 10^8), the substraction of 
1 - cos(x) results in substraction cancellation, where the subtraction of two nearly
equal numbers results in a loss of significant digits in the result. This leads to a 
result of 0 rather than the expected 1/2. 

This loss of precision occurs when the difference between the two numbers is smaller 
than the smallest representable number, which is on the order of 10^-16 for double 
precision floating-point numbers.
'''