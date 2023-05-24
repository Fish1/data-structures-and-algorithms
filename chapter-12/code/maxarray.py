def max(arr):
    if len(arr) == 1:
        return arr[0]

    subset = max(arr[1:])

    if arr[0] > subset:
        return arr[0]
    else:
        return subset

myarr = [ 1, 2, 3, 7, 3, 4, 2, 9, 3, 2, 1 ]

print(max(myarr))
