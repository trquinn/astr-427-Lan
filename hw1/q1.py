import numpy as np

'''
Q1: Floating point representation

For the float data type, write a program to empirically (i.e., by
performing tests on the results of addition and subtraction operations
within your program) determine the following “Machine constants” for
your computer:
(a) The smallest epsilon such that 1.0 − epsilon != 1.0
(b) The smallest  such that 1.0 +  6 = 1.0
(c) The maximum representable number
(d) The minimum representable positive number
Provide all the above answers to better than a factor of 2, and
comment on why the numbers you get are expected based on the
IEEE 754 representation.
'''


# Part A: Find the smallest epsilon such that 1.0 - epsilon != 1.0
epsilon_a = 1.0
while (1.0 - epsilon_a/2.0) != 1.0:
    epsilon_a /= 2.0

# Part B: Find the smallest epsilon such that 1.0 + epsilon != 1.0
epsilon_b = 1.0
while (1.0 + epsilon_b/2.0) != 1.0:
    epsilon_b /= 2.0

# Part C: Find the maximum representable number
max_num = 1.0
while (max_num * 2.0) != float('inf'):
    max_num *= 2.0

# Part D: Find the minimum representable positive number
min_num = 1.0
while (min_num/2) > 0:
    min_num /= 2 

print(f'(a) Smallest epsilon such that 1.0 - epsilon != 1.0: {epsilon_a:.3E}')
print(f'(b) Smallest epsilon such that 1.0 + epsilon != 1.0: {epsilon_b:.3E}')
print(f'(c) Maximum representable number: {max_num:.3E}')
print(f'(d) Minimum representable positive number: {min_num:.3E}')


'''
Output:

(a) Smallest epsilon such that 1.0 - epsilon != 1.0: 1.110E-16
(b) Smallest epsilon such that 1.0 + epsilon != 1.0: 2.220E-16
(c) Maximum representable number: 8.988E+307
(d) Minimum representable positive number: 4.941E-324



Explanation:

These values are consistent with the IEEE 754 double-precision floating-point format, which 
uses 64 bits to represent a number: 1 bit for the sign, 11 bits for the exponent, and 52 
bits for the fraction (significand). Given the 52 bits for the fraction and an implicit 
leading bit (due to the normalization of values), there are effectively 53 bits of precision 
for the significand. This explains why the smallest ε that can alter the value of 1.0 when 
added (Part B) closely matches 2^(-52), and why the smallest ε that can alter the value of 
1.0 when subtracted (Part A) is approximately half of that, due to the subtraction operation's 
behavior in floating-point arithmetic.

The maximum representable number is consistent with the limits imposed by the exponent's size 
(11 bits), allowing for exponents up to 2046 (since exponents are stored with an offset of 1023 
and one value is reserved for infinity), which explains the magnitude of the largest number 
before overflow occurs.

The minimum representable positive number is a result of the format's ability to represent 
denormalized numbers, which allow for extremely small values at the cost of precision. This 
enables the representation of values as small as 5e-324, close to the limit of double-precision 
floating-point arithmetic.
'''