from functools import *
n = int(input())
numbers = [reduce(lambda x, y: x * y, range(1, i + 1)) for i in range(1, n + 1)]
print(sum(numbers))