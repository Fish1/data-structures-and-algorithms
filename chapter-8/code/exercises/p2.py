
def first_duplicate(arr):
    counts = {}

    for c in arr:
        curr = counts.get(c)
        if curr == None:
            counts[c] = 1
        else:
            return c

    return None

x = first_duplicate(["a", "b", "c", "d", "c", "e", "f"])
print(x)

