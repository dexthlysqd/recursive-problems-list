n = int(input())
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
if n == 0:
    print(1)
else:
    print(count_digits(n))
