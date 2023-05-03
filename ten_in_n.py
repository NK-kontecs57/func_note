def ten_in_n():
    n = int(input())
    return [10 ** i for i in range(n)]
print(*ten_in_n())