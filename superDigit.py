# Operations on super integer algorithm
import math
import sys

# Function to get the sum of the digits of the single values
def sum_digit(n):
    if n < 10:      #check if it's a single value and return it
        return n
    else:         #If the value of n is not less than 10, we will calculate the sum and iterate through it
        s = sum([int(x) for x in str(n)])
        return sum_digit(s)

# Super digit function to compute return the calculated super digit as an integer.
def super_digit(n, k):
    p = k * sum_digit(int(n))
    return sum_digit(p)

# Output n and k       
print(super_digit(n, int(k)))