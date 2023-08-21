from functools import reduce
import math

numbers = [2, 3, 5, 6, 7, 9, 10, 11]

# 1. Fibonacci sequence using recursion
def fibonacci(n):
  return reduce(lambda r,i: r+[r[-1]+r[-2]], [0,1]*n, [0,1])[:n]

# 2. Volume of a sphere
def volumeSphere(radius):
    return round(((4/3) * math.pi * radius**3),2)

# 3. Calculate the sum of the squares of the odd numbers
result = sum([n**2 for n in numbers if n % 2 == 1])

# 4. Filter even numbers
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))


