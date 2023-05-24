
def is_subset(original, check):
    exists = {}
    for c in original:
        exists[c] = True

    for c in check:
        if exists.get(c) == None:
            return False

    return True

a1 = ["a", "b", "c", "d", "e", "f"]

a2 = ["d", "e", "f"]

print(is_subset(a1, a2))

a3 = ["d", "e", "f", "g"]

print(is_subset(a1, a3))

