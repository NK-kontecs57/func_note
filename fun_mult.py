from functools import *
m, n = float(input()), float(input())
fun_mult = lambda x, y: x * y
result = reduce(fun_mult, [i for i in range(int(m) + 1, int(n) + 1) if i % 2 != 0], 1)
print(result)