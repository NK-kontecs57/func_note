from functools import reduce
m, n = int(input()), int(input())
fact = lambda x: reduce(lambda x, y: x * y, range(1, x + 1))
numbers = [i for i in range(m, n + 1) if fact(i) < n]
print(*numbers)