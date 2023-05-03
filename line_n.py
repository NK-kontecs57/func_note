def line_n():
    n = int(input())
    return [i for i in range(1, n + 1)]
print(*line_n())
