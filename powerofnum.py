a = int(input("a = "))
b = int(input("b = "))
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)
print(power(a, b))
