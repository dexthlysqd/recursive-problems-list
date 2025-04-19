n = int(input())
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)
result = sum_natural(n)
print(result)