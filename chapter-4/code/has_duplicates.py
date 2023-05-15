
my_array = [4, 5, 2, 9, 3, 44, 55, 0, 1]

# O(N^2)
# For each element in the array we need to loop over the array again
def has_duplicate_slow(array):
    for (index_1, value_1) in enumerate(array):
        for (index_2, value_2) in enumerate(array):
            if index_1 != index_2 and value_1 == value_2:
                return True
    return False

# O(N)
# in this implementation we only need to loop over the array once
# we can use a hashmap to check if there exissts a duplicate
# access to a hash map is O(1)
def has_duplicate_fast(array):
    contains = {}
    for value in array:
        if value in contains.keys():
            return True
        else:
            contains[value] = True
    return False

print(has_duplicate_slow(my_array))
print(has_duplicate_fast(my_array))
