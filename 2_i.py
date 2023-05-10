n, m = int(input()), int(input())
numbers = [2 ** i for i in range(n, m + 1)]
print(*numbers)