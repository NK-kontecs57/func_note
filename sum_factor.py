from math import factorial as fac
numbers = map(lambda x: fac(x), range(1, int(input()) + 1))
print(numbers)