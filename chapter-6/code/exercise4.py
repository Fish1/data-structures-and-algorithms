mystring = "Helloworld"

# worst case = O(N)
# average case = O(N)
# best case = O(N)
def contains_x(str):
    found_x = False

    for c in str:
        if c == 'X':
            found_x = True

    return found_x

# worst case = O(N)
# average case = O(N / 2)
# best case = O(1)
def contains_x_fast(str):
    for c in str:
        if c == 'X':
            return True

    return False

mystring = "HelloXworld"
print(contains_x(mystring))
print(contains_x_fast(mystring))


