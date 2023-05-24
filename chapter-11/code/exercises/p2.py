
def get_even(arr):
    if len(arr) == 0:
        return []

    if arr[0] % 2 == 0:
        return [arr[0]] + get_even(arr[1:])
    else:
        return get_even(arr[1:])


mydata = [1, 2, 3, 4, 5, 6, 7, 8]

print(get_even(mydata))
