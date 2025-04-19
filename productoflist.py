arr = input()
clean_arr = arr.replace(",", " ")
numbers = list(map(int, clean_arr.split()))
def product_list(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * product_list(arr[1:])
print(product_list(numbers))