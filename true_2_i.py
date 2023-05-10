n, m = int(input()), int(input())
numbers = [i for i in range(n, m + 1) if i ** 2 < m + 1]
print(*numbers)