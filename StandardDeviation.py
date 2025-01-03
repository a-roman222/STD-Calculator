# Topic Challenge - Module 4A - Functions
# Student: Andres Roman
# Studen ID: 0374136
# Date: Septermber 14, 2024

import math

def StdDev(numbers):
    """ Returns a standard deviation of one array of values."""
    N = len(numbers)
    if N < 2:
        raise ValueError("At least two numbers are required to calculate standard deviation.")

    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    tmp = 0

    for x in numbers:
        tmp = tmp + ((x - mean) ** 2)

    tmp = tmp / (N -1)

    return { 'std': math.sqrt(tmp), 'avg': mean }

