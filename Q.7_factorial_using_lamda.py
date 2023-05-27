'''
Q7. Calculate the factorial of a number using lambda function.
'''
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# Example usage
number = 5
result = factorial(number)
print(result)
